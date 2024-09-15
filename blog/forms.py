from django import forms
from blog.models import Commentary


class CommentaryCreateForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
