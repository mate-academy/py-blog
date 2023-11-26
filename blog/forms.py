from django import forms
from .models import Commentary
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["content"].label = ""

    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "cols": 40}),
        }
