from .models import Commentary
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("post", "user", "content")
        widgets = {"user": forms.HiddenInput(),
                   "post": forms.HiddenInput()}
