
from book_crud.models import Book,User,Author,Library
from rest_framework import serializers
from django.core.exceptions import ValidationError


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    image= serializers.ListField(child=serializers.ImageField())
    class Meta:
        model = Book
        fields = ["id","image","name","author","publication_date","rating"]

    def validate_rating(self,value):
        if value < 0 or value >= 10:
            raise serializers.ValidationError("rating should be between 0 to 10 ")
        return value

    def to_representation(self, instance):
        representation = super(BookSerializer, self).to_representation(instance)
        author_list = []
        for author in instance.author.all():
            author_list.append(author.name)
            representation['author'] = author_list
        return representation

    def create(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.author = validated_data.get('author',instance.author)
        instance.image = validated_data.get('image',instance.image)
        # super().create(validated_data)
        # instance = Book.objects.create(**validated_data,name=name,author=author,image=image)
        instance.save()
        return instance
        # book_serializer =
    #     print("validated_data-------------",validated_data)
    #     author_data = validated_data.pop('author')
    #     image_data = validated_data.pop('image')
    #     book = Book.objects.create(**validated_data)
    #     print("book ------------------",book)
    #     print("author_data-----------------",author_data)
    #     print("image_data--------------",image_data)
    #     return Book.objects.create(**validated_data)
        # return validated_data


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



    