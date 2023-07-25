import re
from book_crud.models import Book,User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_rating(self,value):
        if value < 0 or value >= 10:
            raise serializers.ValidationError("rating should be between 0 to 9.9 ")
        return value


class UserSerializer(serializers.Serializer):

    def validate_length(value):
        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)
        if length > 10:
            raise ValidationError(
                _('phone number is above 10 digits')
            )

    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type" : "password"})
    phone_number = serializers.RegexField("[0-9]{10}",validators=[validate_length])

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    class Meta:
        model = User
        fields = ["username","email","password","phone_number"]
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=["username","email"]
            )
        ]

    def validate_email_address(email):
        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            print(f"The email address {email} is not valid")
            return False


    