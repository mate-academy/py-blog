from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Comment
        exclude = ("user", "post")
