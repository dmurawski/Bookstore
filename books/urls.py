from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", views.BookDetialView.as_view(), name="book_detail"),
    path(
        "search/",
        views.SearchResultsListView.as_view(),
        name="search_results",
    ),
    path(
        "category/<slug:category_slug>/",
        views.category_books,
        name="category_books",
    ),
]
