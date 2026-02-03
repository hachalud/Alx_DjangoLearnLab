from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="Aldous Huxley")
        
        # Create books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author1)
        self.book3 = Book.objects.create(title="Brave New World", publication_year=1932, author=self.author2)

        # API client
        self.client = APIClient()
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
    def test_book_detail(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2026,
            'author': self.author2.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2026,
            'author': self.author2.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_update_book(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': '1984 Updated'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, '1984 Updated')
    def test_delete_book(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())
    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author__name=George Orwell'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Brave'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Brave New World')

    def test_order_books_by_year_desc(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 1949)
