from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea
            (attrs={"rows": 3, "placeholder": "Write your comment here..."}),
        }
