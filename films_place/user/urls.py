from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('register/', views.UserCreationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]
