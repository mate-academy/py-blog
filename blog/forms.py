from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={'rows': 4})}
