from django import forms

from blog.models import Commentary


class CommentaryCreationForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = [
            "content",
        ]
