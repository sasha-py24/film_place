from django.db import models
from core.models import TimeStampedMixin



class Genre(TimeStampedMixin):
    name = models.CharField(max_length=100)




