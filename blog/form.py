from django import forms


class CommentaryCreateForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.Textarea(attrs={"rows": 3, "style": "width: 50%"}),
    )
