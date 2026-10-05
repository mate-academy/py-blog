from django import forms

from blog.models import Commentary


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": "Your comment"}
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3}),
        }
