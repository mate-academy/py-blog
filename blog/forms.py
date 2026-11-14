from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    class Meta:
        model = Commentary
        fields = ["content"]

    def clean(self):
        cleaned_data = super().clean()
        if not self.user or not self.user.is_authenticated:
            raise forms.ValidationError("You must be logged in to comment.")
        return cleaned_data
