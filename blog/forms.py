from django import forms
from .models import Commentary, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
