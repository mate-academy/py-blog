from django import forms
from django.contrib.auth import get_user_model

from blog.models import Commentary


User = get_user_model()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
