from django import forms
from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["user", "post", "content"]
        widgets = {
            "user": forms.HiddenInput(),
            "post": forms.HiddenInput(),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Leave a comment...", "class": "textarea"
                }
            ),
        }
