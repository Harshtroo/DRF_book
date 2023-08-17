from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from book_create.models import Book

class CreateBookViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_bulk_create_books(self):
        data = {
            "name": "Book1,Book2,Book3",
            "author": "1,2,3",
            # Add image data if needed
        }

        response = self.client.post('/path/to/your/endpoint/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # Check if 3 books were created

    def test_invalid_payload(self):
        data = {
            "name": "Book1,Book2",
            "author": "1,2,3",
            # Add image data if needed
        }

        response = self.client.post('/path/to/your/endpoint/', data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 0)  # No books should be created

    # Add more test cases if needed...
