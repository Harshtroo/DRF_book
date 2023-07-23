from django.urls import path, include
from book_crud import views


urlpatterns = [
    path("create_book/",views.create_book,name="create_book"),
    path("book_list/",views.book_list,name="book_list"),
    path("book_update/<int:pk>/",views.book_update,name="book_update"),
    path("book/delete/",views.book_delete,name="book_delete"),
]