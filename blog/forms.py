from django import forms

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "border",
                "style": "color: white",
                "rows": 5,
                "cols": 80,
            }
        )
    )

    class Meta:
        model = Commentary
        fields = ("content",)
