from django import forms

from blog.models import Comment


class CommentaryCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
