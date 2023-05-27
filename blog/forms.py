from django import forms


class CommentaryCreateForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.Textarea(
            attrs={
                "cols": 200,
                "rows": 3,
                "style": "width: 100%; resize: vertical;",
                "placeholder": "Enter your comment here...",
                "class": "form-control"
            }
        )
    )
