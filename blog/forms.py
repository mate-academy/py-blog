from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False
    )

    class Meta:
        model = Commentary
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content", None)
        if not content:
            raise forms.ValidationError("You need to write something first.")
        return content
