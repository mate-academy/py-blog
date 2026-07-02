from django import forms
from django.core.exceptions import ValidationError
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def clean(self):
        cleaned_data = super().clean()
        user = self.initial.get("user")

        if user is None or not user.is_authenticated:
            raise ValidationError("You must be logged in to leave a comment.")

        return cleaned_data
