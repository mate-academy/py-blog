from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"row": 5}), label=""
    )

    class Meta:
        model = Commentary
        fields = ("content",)
