from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Commentary

# class CreateCommentForm():
#     content = forms.CharField(label="", max_length=500, widget=forms.Textarea)


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = [
            "content",
            "user",
            "post",
        ]
        labels = {"content": ""}
        widgets = {
            "post": forms.HiddenInput(),
            "user": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def is_valid(self) -> bool:
        is_valid = super().is_valid()
        # if not is_valid:
        #     return False
        if not (is_valid and self.user and self.user.is_authenticated):
            self.add_error("content", "Plsease, Log In")
            return False
            # return self.form_invalid(self)
        return True

    # def clean(self):
    #     if not (self.user and self.user.is_authenticated):
    #         # Or you might want to tie this validation to the password1 field
    #         raise forms.ValidationError("Passwords did not match")
    #     return self.cleaned_data
