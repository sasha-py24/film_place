from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, UserLoginForm


class UserLoginView(LoginView):
    template_name = "user/user_login.html"
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/"


class UserRegisterView(CreateView):
    template_name = "user/user_creation.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Акаунт успішно створено!")
        return response

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs["class"] = "form-control"
        return form
