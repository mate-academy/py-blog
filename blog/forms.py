from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        label="Content", widget=forms.Textarea(attrs={"class": "form-control"})
    )

    def __init__(self, *args, user=None, post=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.post = post

    def clean(self):
        cleaned_data = super().clean()
        if self.user is None or not self.user.is_authenticated:
            raise forms.ValidationError("You must be logged in to comment.")
        if self.post is None:
            raise forms.ValidationError("Invalid post.")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        instance.post = self.post
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Commentary
        fields = ["content"]
