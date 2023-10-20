from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)

        widgets = {
            "content": forms.TextInput(
                attrs={"placeholder": "Please, leave your comment"}
            )
        }
        labels = {
            "content": False
        }
