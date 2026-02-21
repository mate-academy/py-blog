from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))

    def clean(self):
        cleaned_data = super().clean()

        if not self.user or not self.user.is_authenticated:
            raise forms.ValidationError("You must login first")

        return cleaned_data

    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {
            "content": "Leave a Comment!",
        }