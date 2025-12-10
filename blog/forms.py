from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from blog.models import Commentary

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
