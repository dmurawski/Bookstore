from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path(
        "books/<uuid:book_id>/review/",
        views.ReviewCreateView.as_view(),
        name="review_create",
    ),
    path(
        "review/edit/<int:pk>/",
        views.ReviewUpdateView.as_view(),
        name="review_edit",
    ),
    path(
        "review/delete/<int:pk>/",
        views.ReviewDeleteView.as_view(),
        name="review_delete",
    ),
    path("", views.UserReviewsView.as_view(), name="reviews"),
]
