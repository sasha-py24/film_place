from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.core.mail import send_mail

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
    model = Movie
    context_object_name = "movies"

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            return cart.movies.all()
        return Movie.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            total_price = sum(movie.price for movie in cart.movies.all())
            context['total_price'] = total_price
        else:
            context['total_price'] = 0
        return context


class CartAddView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs.get('pk')
        try:
            movie = Movie.objects.get(pk=movie_id)
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.movies.add(movie)
            return redirect('movie:cart')
        except Movie.DoesNotExist:
            return redirect('movie:home')


class CartRemoveView(LoginRequiredMixin, TemplateView):
    template_name = "cart/cart_details.html"
    success_url = "/cart"
    
    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=movie_id)
        cart = Cart.objects.filter(user=request.user).first()
        if cart and movie in cart.movies.all():
            cart.movies.remove(movie)
        return redirect('movie:cart')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            context['movies'] = cart.movies.all()
            total_price = sum(movie.price for movie in cart.movies.all())
            context['total_price'] = total_price
        else:
            context['movies'] = []
            context['total_price'] = 0
        return context
