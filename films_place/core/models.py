from django.db import models


class TimeStampedMixin(models.Model):
    # не зможеми ніяк змінити, важливо викор параметри
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # можем змінити
    # date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
