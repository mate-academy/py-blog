from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "text": "Add your comment",
        }
        widgets = {
            "text": forms.Textarea(
                attrs={"rows": 1, "placeholder": "Write a comment..."}
            ),
        }
