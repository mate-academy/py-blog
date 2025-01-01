from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]  # Только поле содержимого комментария
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your comment here...",
                    "rows": 3,
                }
            ),
        }
