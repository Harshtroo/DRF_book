from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from book_crud.models import Book,Author
from rest_framework import status


class CreateBookViewTest(TestCase):

    def setUp(self):
        self.url = reverse("bulk_create_book")
        self.client = APIClient()
        Author.objects.create(name="David Beazley")
        Author.objects.create(name="Wes Mckinney")
        self.payload = {
            "name": "Book1,Book2",
            "author": "1,2",
            "image":[
                open("/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg","rb"),
                open("/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg","rb"),
            ]

        }


    def test_create_book_with_valid_payload(self):
        response = self.client.post(self.url, data=self.payload, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_with_invalid_payload(self):

        data = {
            "name": "Book1,Book2",
            "author": "1",
            "image": [
                open(
                    "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg",
                    "rb"),
            ]
        }
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 0)

    def test_single_create_book(self):
        data = {
            "name": "Book1",
            "author": "1",
            "image": [
                open(
                    "/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg",
                    "rb"),
            ]
        }
        response = self.client.post(self.url, data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

    def test_create_book_with_missing_data(self):

        data = {
            "name": "Book1",
            "author": "1",
        }
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 0)

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
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 0)


