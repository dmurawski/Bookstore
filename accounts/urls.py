from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.SignupPageView.as_view(), name="signup"),
    path("profile/view/", views.ProfileView.as_view(), name="profile"),
]
