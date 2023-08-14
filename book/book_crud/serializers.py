
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
            raise serializers.ValidationError("rating should be between 0 to 9.9 ")
        return value

    def to_representation(self, instance):
        representation = super(BookSerializer, self).to_representation(instance)
        author_list = []
        for author in instance.author.all():
            author_list.append(author.name)
            representation['author'] = author_list
        return representation

    # def create(self, validated_data):
    #     image = validated_data.pop('image', [])
    #     instance = super().create(validated_data)
    #
    #     for image in image:
    #         instance.image.create(image=image)
    #
    #     return instance

    def validate(self,validate_data):
        # validate_data["id"] = str(uuid.uuid4())
        print("validate_data-----",validate_data)
        print("self-------------",self.initial_data)
        # book =Book(validate_data)
        # book.save()
        return self.initial_data




    # def create(self,validate_data):
    #     breakpoint()
    #     for key,value in validate_data.items():
    #         if key == "image":
    #             for image in value:
    #                 add_image = Book.objects.create(image=image)
    #                 add_image.save()
    #     return validate_data




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



    