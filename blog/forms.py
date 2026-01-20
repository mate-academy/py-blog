from django import forms

from .models import Commentary


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        max_length=255,
        widget=forms.Textarea(
            attrs={"cols": 50, "rows": 3, "placeholder": "Write here..."}
        ),
    )

    class Meta:
        model = Commentary
        fields = ["content", ]
