from django import forms

from blog.models import Commentary


class CommentaryCreateForm(forms.Form):
    model = Commentary
    fields = ["content"]
