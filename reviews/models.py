from django.db import models
from books.models import Book
from django.contrib.auth import get_user_model


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.TextField(blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"Review for {self.book.title} by {self.author.username}"
