from django import forms

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        label="Add new comment",
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20})
    )

    class Meta:
        model = Commentary
        fields = ("content",)
