from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        if not (self.user and self.user.is_authenticated):
            raise forms.ValidationError(
                "Only authorized users can post comments."
            )
        return cleaned_data
