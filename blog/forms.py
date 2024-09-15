from django import forms

from blog.models import Commentary


class CommentaryCreationForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 3, "placeholder": "Write your comment here..."}
        )
    )

    class Meta:
        model = Commentary
        fields = [
            "content",
        ]
