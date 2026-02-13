from django.test import TestCase, Client
from django.urls import reverse
from .models import Book, Category

class BookTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Fiction")
        self.book = Book.objects.create(
            title="Test Book",
            isbn="1234567890123",
            publication_year=2022,
            description="Test Description"
        )
        self.book.categories.add(self.category)
        self.list_url = reverse('book_list')
        self.delete_url = reverse('book_delete', args=[self.book.pk])

    def test_book_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'Test Book')

    def test_book_delete_view_get(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_delete.html')

    def test_book_delete_view_post(self):
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
