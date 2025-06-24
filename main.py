# from django.db import models
# from django.contrib.auth.models import User
#
# class Genre(models.Model):
#     name = models.CharField(max_length=100)
#
# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     genre = models.ManyToManyField(Genre)
#     poster = models.ImageField(upload_to='posters/')
#     trailer_url = models.URLField(blank=True, null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class Catalog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     movies = models.ManyToManyField(Movie)
#
# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     movies = models.ManyToManyField(Movie)
#
# class Purchase(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     purchase_date = models.DateTimeField(auto_now_add=True)

