from django.forms import ModelForm
from .models import Commentary, Post


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ("user", "content", "post",)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("owner", "title", "content",)
