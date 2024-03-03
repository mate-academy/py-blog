from django import forms

from blog.models import Commentary


class CreateCommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {"content": "Add comment:"}
