from django.forms import ModelForm
from django.forms.widgets import Textarea

from blog.models import Commentary


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {"content": ""}
        widgets = {
            "content": Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control",
                }
            )
        }
