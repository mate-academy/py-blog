from django import forms

from blog.models import Commentary
from crispy_forms.helper import FormHelper


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean(self):
        cleaned_data = super().clean()
        if self.user is None or self.user.is_anonymous:
            raise forms.ValidationError(
                "You must be logged in to post a comment"
            )
        return cleaned_data
