from django import forms

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Commentary
        fields = ("content", )
