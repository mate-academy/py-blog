from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea)

    class Meta:
        model = Commentary
        fields = ("content",)
