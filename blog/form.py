from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Add a comment..."}
            ),
        }
