from django import forms


class CommentaryForm(forms.Form):
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
