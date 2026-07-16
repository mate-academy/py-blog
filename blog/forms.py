from django import forms

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        fields = ["content"]
        model = Commentary
        labels = {"content": "Add a new comment"}
