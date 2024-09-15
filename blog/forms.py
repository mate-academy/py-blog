from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "custom-textarea"}),
    )

    class Meta:
        model = Commentary
        fields = ["content"]
