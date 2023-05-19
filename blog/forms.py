from django import forms

from blog.models import Commentary


class CommentaryCreateForm(forms.Form):
    class Meta:
        model = Commentary
        fields = ["content"]
