from django.db import models
from datetime import date

class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(default=date.today)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name