from core.models import TimeStampedMixin
from django.db import models


class Genre(TimeStampedMixin):
    name = models.CharField(max_length=100)
