from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["text"]
        labels = {
            "content": "",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Napisz swój komentarz tutaj...",
                    "class": "form-control",
                }
            ),
        }
