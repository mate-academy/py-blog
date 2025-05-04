from django import forms

from blog.models import Commentary


class CommentaryModelForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Write your comment here...",
                    "class": "form-control",
                }
            )
        }
