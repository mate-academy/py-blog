from django import forms

from blog.models import Commentary


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
