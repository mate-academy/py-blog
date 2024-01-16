from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"cols": 60, "rows": 3}
        ),
        label=""
    )

    class Meta:
        model = Commentary
        fields = ["content"]
