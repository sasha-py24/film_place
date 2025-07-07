from django.shortcuts import render
from .models import Movie, Cart, Genre
from .forms import MovieCreationForm


from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class MovieListView(ListView):
    template_name = 'index.html'
    model = Movie
    context_object_name = 'movies'  



class MovieCreationView(CreateView):
    template_name = 'movie_creation.html'
    model = Movie
    form_class = MovieCreationForm
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)





