from crispy_forms.helper import FormHelper
from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.helper = FormHelper()

    def clean(self):
        cleaned_data = super().clean()
        if self.user is None or self.user.is_anonymous:
            raise forms.ValidationError("Please login")
        return cleaned_data

    class Meta:
        model = Commentary
        fields = ["content"]
