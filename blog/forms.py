from typing import Any

from django import forms
from django.contrib.auth.base_user import AbstractBaseUser

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": "Add a new comment"}

    def __init__(self, *args, user=None, **kwargs) -> None:
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        if not (self.user and self.user.is_authenticated):
            raise forms.ValidationError(
                "Only authenticated users can leave comments"
            )
        return cleaned_data
