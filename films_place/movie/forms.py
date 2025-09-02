from django import forms
from django.core.mail import send_mail

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


class CartAddForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["movies"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def clean_movies(self):
        movies = self.cleaned_data["movies"]
        if movies.count() > 10:
            raise forms.ValidationError("You can add up to 10 movies to the cart")
        return movies

    def save(self, commit=True):
        cart = super().save(commit=False)
        if self.request and self.request.user.is_authenticated:
            cart.user = self.request.user

            # Відправка листа
            send_mail(
                subject="New Order Received",
                message=f"User {self.request.user.username} placed an order with {cart.movies.count()} movie(s).",
                from_email="trankosergij@gmail.com",
                recipient_list=["sakuzpol@gmail.com"],
                fail_silently=False,
            )

        if commit:
            cart.save()
            self.save_m2m()  
        return cart