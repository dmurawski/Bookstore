from django.views import generic
from .models import Review, Book
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth import get_user_model


class ReviewCreateView(generic.CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ["review"]

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        form.instance.book = book
        form.instance.author = self.request.user
        self.success_url = reverse_lazy(
            "books:book_detail",
            kwargs={"pk": book.pk},
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        context["book"] = book
        return context


class ReviewUpdateView(generic.UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_edit.html"

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("reviews:reviews")


class ReviewDeleteView(generic.DeleteView):
    model = Review
    template_name = "reviews/review_delete.html"
    context_object_name = "review"

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("reviews:reviews")


class UserReviewsView(generic.ListView):
    model = Review
    template_name = "reviews/reviews.html"
    context_object_name = "reviews"
    paginate_by = 10

    def get_queryset(self):
        user = get_user_model().objects.get(
            username=self.request.user.username,
        )
        return Review.objects.filter(author=user)
