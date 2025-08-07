from django import forms

from .models import Movie, Cart
from user.models import TempUser, User


class MovieCreationForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "description", "price", "poster", "trailer_url"]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0 or price > 10000:
            raise forms.ValidationError("price must be between 0 and 10000")
        return price


class CartAddForm(forms.Form):
    class Meta:
        model = Cart
        fields = ["movies"]

    def __init__(self, *args, **kwargs):
        self.instance.user = kwargs.pop('user', None)
        self.instance.temp_user = kwargs.pop('temp_user', None)
        self.product = kwargs.pop('product')
        super().__init__(*args, **kwargs)
        self.instance.temp_user = self.temp_user
        self.instance.user = self.user
        self.instance.product = self.product


    def clean_movies(self):
        movies = self.cleaned_data["movies"]
        if movies.count() > 10:
            raise forms.ValidationError("You can add up to 10 movies to the cart")
        return movies

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.user = self.request.user
        if commit:
            cart.save()
        return cart

