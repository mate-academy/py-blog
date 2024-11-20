from django import forms

from .models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Write Your commentary here",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Commentary
        exclude = ("user", "post", "created_time")
