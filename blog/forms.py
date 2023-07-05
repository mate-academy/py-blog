from django import forms

from .models import Commentary


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
