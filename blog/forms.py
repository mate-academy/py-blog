from django import forms

from blog.models import Commentary


class CommentCreate(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "Add new comment",
        }
