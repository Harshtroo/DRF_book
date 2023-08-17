import pytest
from  rest_framework.test import APIClient
from rest_framework import status
from book_crud.models import Book

@pytest.mark.django_db
def bulk_create_book():
    client = APIClient()
    url = "http://127.0.0.1:8000/bulk_create_book/"

    payload = [
        {
            "name": "Python Pocket Reference",
            "author": 2,
            "image": "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51HuYEwAl2L._SX258_BO1204203200_.jpg"
        },
        {
            "name": "Python Crash Course",
            "author": 2,
            "image": "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51HuYEwAl2L._SX258_BO1204203200_.jpg"
        }
    ]
    response = client.post(url,payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.count() == 2
