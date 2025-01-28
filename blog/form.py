from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 4,
                   "cols": 40
                   }
        )
    )
