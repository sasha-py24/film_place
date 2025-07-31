from django import forms
from .models import Movie, Genre, Cart


class MovieCreationForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'price', 'poster', 'trailer_url']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0 or price > 10000:
            raise forms.ValidationError('price must be between 0 and 10000')
        return price



        