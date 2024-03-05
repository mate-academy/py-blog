from django import forms

from blog.models import Post


class CommentCreationForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Write your comment"}),
    )


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
        )
