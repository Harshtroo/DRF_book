from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.ManyToManyField(Author)
    publication_date = models.DateField(default=date.today)
    rating = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=50, unique=True)
    book = models.ForeignKey("Book",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length = 10)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.username
