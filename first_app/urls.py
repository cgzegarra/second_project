from django.urls import path

from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('image/', views.image),
    path('webpages/', views.webpages),
    path('form_name/', views.form_name),
    path('new_user/', views.new_user_form),
    path('users/', views.users),
    path('relative/', views.relative),
    path('other/', views.other),
    path('other_three/', views.other_three, name='other_three'),
    path('base_other/', views.base_other, name='base_other'),
    path('base_home/', views.base_home, name='base_home')
]