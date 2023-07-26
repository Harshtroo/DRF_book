from django.urls import path, include
from book_crud import views


urlpatterns = [
    path("",views.home,name="home"),
    path("get_create_book/",views.get_create_book,name="get_create_book"),
    path("create_book/",views.create_book,name="create_book"),
    path("get_book_list/",views.get_book_list,name="get_book_list"),
    path("book_list/",views.book_list,name="book_list"),
    path("get_update_data/<int:pk>/",views.get_update_data,name="get_update_data"),
    path("book_update/<int:pk>/",views.book_update,name="book_update"),
    path("book_delete/<int:pk>/",views.book_delete,name="book_delete"),
    path("get_create_user/",views.get_create_user,name="get_create_user"),
    path("create_user/",views.create_user,name="create_user"),
    path("get_user_list/",views.get_user_list,name="get_user_list"),
    path("user_list/",views.user_list,name="user_list"),
]