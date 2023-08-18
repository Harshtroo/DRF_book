import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from book_crud.models import Author
# from book_crud.test.factories import BookFactory
from book_crud.models import Book


@pytest.mark.django_db
class TestCreateBulkBook:

    def setup_method(self):
        self.client =APIClient()
        self.url = reverse("bulk_create_book")

    def test_bulk_create_book(self):
        Author.objects.create(name="David Beazley")
        Author.objects.create(name="Wes Mckinney")
        data = {
            "name": "Book1,Book2",
            "author": "1,2",
            "image": [
                open(
                    "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg",
                    "rb"),
                open(
                    "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg",
                    "rb"),
            ]
        }

        response = self.client.post(self.url, data, format='multipart')
        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.count() == 2

    def test_single_create_book(self):
        Author.objects.create(name="David Beazley")
        data = {
            "name": "Book1",
            "author": "1",
            "image": [
                open(
                    "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg",
                    "rb"),
            ]
        }
        response = self.client.post(self.url, data, format="multipart")
        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.count() == 1

    def test_create_book_with_missing_data(self):
        data = {
            "name": "Book1",
            "author": "1",
        }
        response = self.client.post(self.url,data,format="multipart")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Book.objects.count() == 0

    def test_create_book_with_invalid_data(self):
        data = {
            "name": "Book1,Book2",
            "author": "1",
            "image": [
                open(
                    "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg",
                    "rb"),
            ]
        }
        response = self.client.post(self.url,data, format="multipart")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Book.objects.count() == 0
