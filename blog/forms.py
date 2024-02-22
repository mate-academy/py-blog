from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content", "post", "user")
        widgets = {"post": forms.HiddenInput(), "user": forms.HiddenInput()}
