from django.db.models.query import QuerySet
from django.views import generic
from .models import Book
from django.contrib.auth import mixins
from django.db.models import Q


class BookListView(
    mixins.LoginRequiredMixin,
    generic.ListView,
):
    model = Book
    context_object_name = "book_list"
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
            Q(title__icontains=query) | Q(author__icontains=query)
        )
