from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "placeholder": "Write your comment..."})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "content",
            Submit("submit", "Add comment")
        )

    def clean(self):
        cleaned_data = super().clean()
        if self.user is None or not self.user.is_authenticated:
            raise forms.ValidationError("Only authorized users can add comments.")
        return cleaned_data
