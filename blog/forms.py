from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Comment"))

    def clean_content(self) -> str:
        content: str = self.cleaned_data["content"]
        if not content.strip():
            raise forms.ValidationError("Content cannot be empty")
        return content
