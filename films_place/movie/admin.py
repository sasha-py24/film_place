from django.contrib import admin

from .models.cart import Cart
from .models.genre import Genre
from .models.movies import Movie

admin.site.register(Movie)
admin.site.register(Cart)
admin.site.register(Genre)
