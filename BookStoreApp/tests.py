from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
# Create your tests here.



class BookViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='erkin', password='am1rov_008')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.book_data = {
            "title": "Python",
            "author": "Hasan Husanov",
            "is_available": True
        }
        self.book = Book.objects.create(owner=self.user, **self.book_data)

    def test_book_list_view(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_create_view(self):
        response = self.client.post('/api/books/create/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_detail_view(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_delete_view(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_book_update_view(self):
        updated_data = {"title": "C++"}
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserBooksViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='erkin', password='am1rov_008')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_books_view(self):
        response = self.client.get('/api/user/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscribeViewTest(TestCase):
    def test_subscribe_view(self):
        client = APIClient()
        response = client.post('/api/subscribe/', {'email': 'amiroverkin999@gmail.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserCreateViewTest(TestCase):
    def test_user_create_view(self):
        client = APIClient()
        user_data = {'username': 'erkin', 'am1rov_008': 'am1rov_008'}
        response = client.post('/api/users/create/', user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
