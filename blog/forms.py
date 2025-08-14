from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.request.user.is_authenticated:
            raise forms.ValidationError("Only authorized users can comment")
        return cleaned_data

    class Meta:
        model = Commentary
        fields = ["content"]
