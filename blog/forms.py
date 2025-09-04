from django import forms

from .models import Commentary, User, Post

class CommentaryForm(forms.ModelForm):
    def __init__(self, *args, user=None, post=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.post = post

    content = forms.CharField(
        widget=forms.Textarea,
        label=""
    )

    class Meta:
        model = Commentary
        fields = ["content"]

    def save(self, commit=True):
        commentary = super().save(commit=False)
        commentary.user = self.user
        commentary.post = self.post
        if self.user.is_authenticated:
            raise forms.ValidationError("Musisz być zalogowany, aby dodać komentarz")
        if commit:
            commentary.save()
        return commentary



