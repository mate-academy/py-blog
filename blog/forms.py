from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": "Add a new comment"}

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()

        if not self.user or not self.user.is_authenticated:
            raise forms.ValidationError(
                "Only authenticated users can comment.")

        return cleaned_data
