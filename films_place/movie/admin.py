from django.contrib import admin
from .models.movies import Movie
from .models.cart import Cart
from .models.genre import Genre


admin.site.register(Movie)
admin.site.register(Cart)
admin.site.register(Genre)










