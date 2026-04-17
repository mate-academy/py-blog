from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Post Comment"))

    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3}),
        }
