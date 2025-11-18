from django import forms
from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": ""}
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 3,
                "class": "form-control bg-white-frost",
            })
        }
