import os
import uuid
from datetime import date

from django.db import models
from django.urls import reverse


def get_default_cover():
    default_cover_path = os.path.join("covers", "default_cover.jpg")
    return default_cover_path


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


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
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Books"
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return f"{self.author} - {self.title}"

    def get_absolute_url(self):
        return reverse("books:book_detail", args=[str(self.id)])
