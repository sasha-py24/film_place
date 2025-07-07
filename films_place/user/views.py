from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView


from .models import User
from .forms import UserRegistrationForm, UserLoginForm


class UserCreationView(CreateView):
    template_name = 'user_creation.html'
    model = User
    form_class = UserCreationForm
    fields = '__all__'
    success_url = '/'


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    success_url = '/'
    form_class = UserLoginForm



