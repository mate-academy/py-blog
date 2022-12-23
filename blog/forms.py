from .models import Commentary
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
