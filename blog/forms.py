from django import forms

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "md-textarea form-control",
                "placeholder": "comment here...",
                "rows": "4",
            }
        )
    )

    class Meta:
        model = Commentary
        fields = ("post", "user", "content")
        widgets = {"user": forms.HiddenInput(), "post": forms.HiddenInput()}
