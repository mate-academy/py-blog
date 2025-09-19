from django import forms
from django.core.exceptions import ValidationError

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.user or not self.user.is_authenticated:
            raise ValidationError("You must log in to leave a comment.")
        return cleaned_data
