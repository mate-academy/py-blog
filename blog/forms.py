from django import forms

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        exclude = ["post", "user", ]
        labels = {
            "content": "",
        }
