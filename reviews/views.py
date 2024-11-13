from django.views import generic
from .models import Review, Book
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class ReviewCreateView(generic.CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ["review"]
    success_url = reverse_lazy("books:book_list")

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        form.instance.book = book
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        context["book"] = book
        return context
