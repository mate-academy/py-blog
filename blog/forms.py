from django import forms
from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Commentary
        exclude = ("user", "post")
