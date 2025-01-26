from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        if not self.user or not self.user.is_authenticated:
            raise forms.ValidationError("You must be "
                                        "logged in to add a comment.")
        if not self.post:
            raise forms.ValidationError("Invalid post.")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.user = self.user
        instance.post = self.post
        instance.save()
        return instance
