from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path(
        "books/<uuid:book_id>/review/",
        views.ReviewCreateView.as_view(),
        name="review_create",
    ),
]
