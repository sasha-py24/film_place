from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import CartAddForm, MovieCreationForm
from .models import Cart, Genre, Movie

__all__ = [
    "MovieListView",
    "MovieDetailView",
    "MovieCreationView",
    "MovieUpdateView",
    "MovieDeleteView",
    "CartView",
    "CartAddView",
    "CartRemoveView",
]


class MovieListView(ListView):
    template_name = "index.html"
    model = Movie
    context_object_name = "movies"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class MovieDetailView(DetailView):
    template_name = "movie/movie_detail.html"
    model = Movie
    context_object_name = "movie"


class MovieCreationView(LoginRequiredMixin, CreateView):
    template_name = "movie/movie_creation.html"
    model = Movie
    form_class = MovieCreationForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "movie/movie_update.html"
    model = Movie
    form_class = MovieCreationForm
    success_url = "/"


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "movie/movie_delete.html"
    model = Movie
    success_url = "/"


class CartView(LoginRequiredMixin, ListView):
    template_name = "cart/cart_details.html"
    model = Movie  # тепер модель — Movie
    context_object_name = "movies"

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            return cart.movies.all()
        return Movie.objects.none()



class CartAddView(LoginRequiredMixin, CreateView):
    template_name = "cart/cart_details.html"
    form_class = CartAddForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class CartRemoveView(LoginRequiredMixin, CreateView):
    template_name = "cart/cart_details.html"
    form_class = CartAddForm
    success_url = '/'



        