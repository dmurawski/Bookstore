from django.views import generic
from .models import Review
from django.urls import reverse_lazy


class ReviewCreateView(generic.CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ["review"]
    success_url = reverse_lazy("book_list")
