from django import forms

from blog.models import Commentary


class CommentaryCreateForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control",
                    "placeholder": "Enter your message...",
                }
            ),
        }
        labels = {"content": ""}
