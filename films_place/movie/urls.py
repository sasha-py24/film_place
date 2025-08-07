from django.urls import path

from .views import *

app_name = "movie"

urlpatterns = [
    path("", MovieListView.as_view(), name="home"),
    path("movies/", MovieListView.as_view(), name="movie_list"),
    path("movie/create/", MovieCreationView.as_view(), name="movie_create"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie/<int:pk>/update/", MovieUpdateView.as_view(), name="movie_update"),
    path("movie/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie_delete"),
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/add/", CartAddView.as_view(), name="cart_add"),
]
