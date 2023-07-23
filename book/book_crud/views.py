from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND
from book_crud.serializers import BookSerializer
from rest_framework.decorators import api_view
from book_crud.models import Book
from rest_framework import status

@api_view(["post"])
def create_book(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
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