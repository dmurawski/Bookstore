from django.views import generic
from .models import Category, Book
from django.contrib.auth import mixins
from django.db.models import Q
from django.shortcuts import render, get_object_or_404


class BookListView(
    mixins.LoginRequiredMixin,
    generic.ListView,
):
    model = Book
    context_object_name = "book_list"
    paginate_by = 6
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetialView(
    mixins.LoginRequiredMixin,
    mixins.PermissionRequiredMixin,
    generic.DetailView,
):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )


class SearchResultsListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(category__name__icontains=query)
        )


def category_books(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    book_list = Book.objects.filter(category=category)
    return render(
        request,
        "books/category_books.html",
        {
            "category": category,
            "book_list": book_list,
        },
    )
