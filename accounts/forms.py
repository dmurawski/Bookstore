from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


#imported CustomUser model via get_user_model from AUTH_USER_MODEL config in settings.py. T

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username"]
