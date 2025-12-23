from django import forms
from .models import Commentary, Post


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Add a comment..."})
    )

    class Meta:
        model = Commentary
        fields = ["content"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["owner"]
