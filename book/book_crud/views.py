from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND
from book_crud.serializers import BookSerializer,UserSerializer,AuthorSerializer,LibrarySerializer
from rest_framework.decorators import api_view
from book_crud.models import Book,User,Author,Library
from rest_framework import status
from django.shortcuts import render
from rest_framework import generics



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

def get_create_library(request):
    books = Book.objects.all()
    return render(request,"create_library.html",{"book":books})

def get_library_list(request):
    return render(request,"library_list.html")

def get_update_library(request,pk):
    library = Library.objects.get(id=pk)
    book = Book.objects.all()
    return render(request, "update_library.html", {"library": library,"books":book})

def get_update_data(request,pk):
    book = Book.objects.get(id=pk)
    authors = Author.objects.all()
    return render(request,"book_edit.html",{"book":book,"authors":authors})

@api_view(["POST"])
def create_author(request):
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def author_list(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


class CreateBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        name_list = serializer.initial_data.get("name").split(",")
        author_list = serializer.initial_data.get("author").split(",")
        image_list = request.FILES.getlist("image")

        for i in range(len(name_list)):
            author_obj =Author.objects.get(id=author_list[i])
            book = Book.objects.create(name=name_list[i],image=image_list[i])
            book.author.add(author_obj)

        headers = self.get_success_headers(serializer.data)
        return Response(
                    {"data":serializer.data,
                     "status":status.HTTP_201_CREATED,
                     "headers":headers})


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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def user_list(request):
    books = User.objects.all()
    serializer = UserSerializer(books, many=True)
    return Response(serializer.data)


class LibraryView(generics.CreateAPIView):
    serializer_class = LibrarySerializer

    def get_serializer(self,*args,**kwargs):
        if isinstance(kwargs.get("data",{}),list):
            kwargs["many"] = True
        return super(LibraryView,self).get_serializer(*args,**kwargs)


@api_view(["GET"])
def library_list(request):
    books = Library.objects.all()
    serializer = LibrarySerializer(books, many=True)
    return Response(serializer.data)

@api_view(["PUT"])
def library_update(request,pk):
    try:
        book = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        return Response({"error": "Library not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = LibrarySerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def library_delete(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "library not found"}, status=status.HTTP_404_NOT_FOUND)
    library.delete()
    return Response({"message": "library deleted successfully"}, status=status.HTTP_204_NO_CONTENT)