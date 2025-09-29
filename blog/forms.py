from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control", "rows": 5, "placeholder": "Write your comment..."}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)  # приймаємо користувача
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))