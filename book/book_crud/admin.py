from django.contrib import admin
from .models import Book,User,Author,Library


admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Library)
