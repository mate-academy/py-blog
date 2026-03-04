from django import forms
from .models import Post, Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "Add a comment",
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
