from django import forms

from blog.models import Comment


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
