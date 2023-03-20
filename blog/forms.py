from django import forms

from blog.models import Commentary


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]