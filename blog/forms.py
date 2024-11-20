from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write comment here...",
                "rows": 4,
                "cols": 10,
            }
        ),
    )

    class Meta:
        model = Commentary
        fields = ["content"]
