from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Commentary


class CommentaryAddForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Commentary
        labels = {"content": "Add your comment:"}
        fields = ("content",)
