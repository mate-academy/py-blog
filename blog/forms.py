from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    """Form for creating a new comment."""
    class Meta:
        model = Commentary
        fields = ["content"]  # Only include the content field

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your comment here..."})
        }
