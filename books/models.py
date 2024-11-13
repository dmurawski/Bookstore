import uuid
import os
from django.db import models
from django.urls import reverse
from datetime import date


def get_default_cover():
    default_cover_path = os.path.join("covers", "default_cover.jpg")
    return default_cover_path


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        editable=False,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(
        upload_to="covers/",
        blank=True,
        default=get_default_cover,
    )
    description = models.TextField(blank=True, default="No description")
    published_date = models.DateField(default=date.today)

    class Meta:
        verbose_name_plural = "Books"
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return f"{self.author} - {self.title}"

    def get_absolute_url(self):
        return reverse("books:book_detail", args=[str(self.id)])
