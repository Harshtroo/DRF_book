from book_crud.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate_rating(self,value):
        if value < 0 or value >= 10:
            raise serializers.ValidationError("rating shoud be between 0 to 9.9 ")
        return value