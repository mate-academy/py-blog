from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 8,
                "cols": 64,
                "placeholder": "...",
            }
        ),
    )
    class Meta:
        fields = ("content", )
        model = Commentary
