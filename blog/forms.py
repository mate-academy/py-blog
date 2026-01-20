from .models import Commentary
from django import forms


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content", ]
