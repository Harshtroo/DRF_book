
from book_crud.models import Book,User,Author,Library
from rest_framework import serializers
from django.core.exceptions import ValidationError


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id","image","name","author","publication_date","rating"]

    def validate_rating(self,value):
        if value < 0 or value >= 10:
            raise serializers.ValidationError("rating should be between 0 to 10 ")
        return value


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ["id","name","book"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email","password","phone_number"]

    def validate_phone_number(self,phone_number):
        if len(str(phone_number)) >= 11:
            raise ValidationError('Phone number is above 10 digits.')
        return phone_number



    