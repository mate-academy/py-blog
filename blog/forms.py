from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        exclude = ["user", "post"]
