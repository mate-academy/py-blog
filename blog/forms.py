from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
