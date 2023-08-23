from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from .models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'second_app/index.html')

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('second_app:index'))

def user_login(request):

    if request.method == 'POST':

        # First get the username and password supplied
        username = request.POST.get('username')    
        password = request.POST.get('password')

        print(username)
        print(password)

        # Django's built-in authentication function
        user = authenticate(username=username, password=password)
        
        if user:

            if user.is_active:
                login(request,user)

                #Send the user back to the homepage.
                return HttpResponseRedirect(reverse('second_app:index'))
            else:
                # If the account is not active
                return HttpResponse("Your account is not active")
        else:
            print("Someone tried to login and failed")
            print(f"They used username: {username} and password: {password}")

            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'second_app/login.html', {})
    
def user_register(request):

    registered: bool = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            # Save the User Form to the database
            user = user_form.save()
            
            # Hash the password
            user.set_password(user.password)
            
            # Update with Hashed Password
            user.save()

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('picture found')
                profile.profile_pic = request.FILES['profile_pic']
            else:
                print('picture not found')

            # Save the profile
            profile.save()

            # Registration Successful
            registered = True
        else:
            # One of the forms or both are invalid.
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request, 'second_app/register.html', { 'user_form': user_form, 
                                                         'profile_form': profile_form, 
                                                         'registered': registered })


def user_list(request):

    users = User.objects.order_by('last_name')


    dict = { 'users' : users, 'profile': { "root" : "root1" } }

    return render(request, 'second_app/users.html', { 'users' : users, 
                                                      'profile': { "root" : "root1" },
                                                      'test': 'hello123'
                                                      })