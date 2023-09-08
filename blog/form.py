from django import forms

from .models import Commentary


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": "Comment"}
