from django.db import models
from user.models import User
from movie.models.movies import Movie



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)