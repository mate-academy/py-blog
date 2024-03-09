from django import forms

from .models import Commentary, Post


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
