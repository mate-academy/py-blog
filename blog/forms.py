from django import forms
from .models import Commentary

class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['content']  # Only include the content field for the comment.
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }