
from django import forms
from django.core import validators

from .models import User

def validate_email(value):
    print("Validate Email: " + value)

    if "gmail.com" not in value:
        print("Raise Error")
        raise forms.ValidationError("Gmail accepted only")

class FormName(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(6)])
    email = forms.EmailField(validators=[validate_email])
    text = forms.CharField(widget=forms.Textarea)

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

