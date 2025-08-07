from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.PositiveIntegerField(null=True)

class TempUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)

    
