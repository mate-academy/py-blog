from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "style": "width: 100%; "
                             "border-radius: 8px; "
                             "border: 1px solid #ccc; "
                             "padding: 10px;",
                }
            ),
        }
