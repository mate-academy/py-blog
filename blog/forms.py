from django import forms
from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content", )
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 4,
                "cols": 60,
                "placeholder": "Type your comment here...",
            })
        }
