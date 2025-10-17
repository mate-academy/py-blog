from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError

from blog.models import Commentary

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Add Comment"))

    def clean_content(self):
        content = self.cleaned_data.get("content", "").strip()
        if not content:
            raise ValidationError("Comment cannot be empty or whitespace")
        return content
