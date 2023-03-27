from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "rows": 4,
            "placeholder": "Add you comment"}
        )
    )

    class Meta:
        model = Commentary
        fields = ("content",)
