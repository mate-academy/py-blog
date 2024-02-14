from .models import Commentary
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3}),
        }
        labels = {
            "content": "Add a new comment",
        }
