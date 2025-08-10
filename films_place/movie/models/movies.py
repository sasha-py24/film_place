from core.models import TimeStampedMixin
from django.db import models


class Movie(TimeStampedMixin):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    trailer_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
