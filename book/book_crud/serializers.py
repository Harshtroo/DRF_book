import re
from book_crud.models import Book,User,Author
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ["id","image","name","author","publication_date","rating"]

    def validate_rating(self,value):
        if value < 0 or value >= 10:
            raise serializers.ValidationError("rating should be between 0 to 9.9 ")
        return value

    def to_representation(self, instance):

        representation = super(BookSerializer, self).to_representation(instance)
        author_list = []
        print("data112--------------",instance.author)
        for author in instance.author.all():
            author_list.append(author.name)
            representation['author'] = author_list
        return representation

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email","password","phone_number"]
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=["username","email"]
            )
        ]

    def validate_length(value):
        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)
        if length > 10:
            raise ValidationError(
                _('phone number is above 10 digits')
            )

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def validate_email_address(email):
        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            print(f"The email address {email} is not valid")
            return False


    