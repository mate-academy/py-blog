from django.contrib.auth import get_user_model

from blog.models import Post, Commentary
from django import forms
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 1}))

    class Meta:
        model = Commentary
        fields = ("content",)
