from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from reviews.models import Review

from .models import Book, Category


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug")
    ordering = ["name"]
    search_fields = ["name", "slug"]


@admin.register(Book)
class BookAdmin(ExportMixin, admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )
    resource_class = BookResource
