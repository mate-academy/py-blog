from django import forms
from .models import Commentary
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super(CommentaryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
