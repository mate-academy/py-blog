from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.Field(label="", widget=forms.Textarea)

    class Meta:
        model = Commentary
        fields = ("content",)
