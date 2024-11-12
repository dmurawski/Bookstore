from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book
from reviews.models import Review


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="review_user",
            email="review_user@email.com",
            password="testpass123",
        )
        cls.book = Book.objects.create(
            title="Test book",
            author="John Doe",
            price="22.88",
        )
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="Very good book!",
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title, "Test book")
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.price, "22.88")

    def test_book_list_view(self):
        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test book")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/132312/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "Very good book!")
        self.assertTemplateUsed(response, "books/book_detail.html")
