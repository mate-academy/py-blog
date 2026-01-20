from django import forms
from django.forms import Textarea

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        exclude = ["user"]
        labels = {
            "content": "",
        }
        widgets = {
            "content": Textarea(attrs={"cols": 20, "rows": 10}),
        }
