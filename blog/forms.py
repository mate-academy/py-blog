from django import forms

from blog.models import Commentary, Post


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "Write a commentary:",
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        labels = {
            "title": "Write a title: ",
            "content": "Write your post:",
        }
