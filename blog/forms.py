from django import forms
from django.core.exceptions import ValidationError

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write a comment..."}
            ),
        }
        labels = {"content": "Your comment"}

    def __init__(self, *args, user=None, post=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.post = post

    def clean(self):
        cleaned_data = super().clean()
        if self.user is None or not self.user.is_authenticated:
            raise ValidationError("Only authorized users can post comments.")
        return cleaned_data

    def save(self, commit=True):
        commentary = super().save(commit=False)
        commentary.user = self.user
        commentary.post = self.post
        if commit:
            commentary.save()
        return commentary
