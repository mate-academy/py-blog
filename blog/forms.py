from django import forms

from .models import Commentary


class CommentaryForm(forms.Form):
    content = forms.CharField()

    class Meta:
        model = Commentary
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content", None)
        if not content:
            raise forms.ValidationError("Add any comment")
        return content
