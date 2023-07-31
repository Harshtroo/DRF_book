from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND
from book_crud.serializers import BookSerializer,UserSerializer,AuthorSerializer
from rest_framework.decorators import api_view
from book_crud.models import Book,User,Author
from rest_framework import status
from django.shortcuts import render


def home(request):
    return render(request,"home.html")

def get_book_list(request):
    return render(request,"book_list.html")

def get_create_book(request):
    return  render(request,"create_book.html")

def get_user_list(request):
    return render(request,"user_list.html")

def get_create_user(request):
    return render(request,"create_user.html")

def get_create_author(request):
    return render(request, "create_author.html")

def get_update_data(request,pk):
    book = Book.objects.get(id=pk)
    
    authors = Author.objects.all()
    print("authors========",authors)
    return render(request,"book_edit.html",{"book":book,"authors":authors})

@api_view(["POST"])
def create_author(request):
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=400)


@api_view(["GET"])
def author_list(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)



@api_view(["POST"])
def create_book(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)

        print("serializer===========",serializer)

        if serializer.is_valid():

            print("serializer===================",serializer)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(["PUT"])
def book_update(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    print("serializer=====",serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def book_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    book.delete()
    return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_user(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

@api_view(["GET"])
def user_list(request):
    books = User.objects.all()
    serializer = UserSerializer(books, many=True)
    return Response(serializer.data)