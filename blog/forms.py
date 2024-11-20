from django import forms

from blog.models import Commentary, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
