from django.contrib import admin

from .models import Book, Category
from reviews.models import Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )
