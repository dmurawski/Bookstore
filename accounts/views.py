from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from reviews.models import Review


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(generic.DetailView):
    model = get_user_model()
    template_name = "accounts/profile_view.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)
