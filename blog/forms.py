from django import forms
from django.forms import Textarea

from blog.models import Commentary


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["content"].label = "Comment section"

    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": Textarea(
                attrs={
                    "rows": "3",
                    "class": "form-control mb-2",
                    "placeholder": "Enter your comment",
                }
            )
        }
