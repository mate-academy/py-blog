from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea
from django.forms.models import ModelForm

from blog.models import Commentary, Post


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {"content": "Post a comment",}
        widgets = {"content": Textarea(attrs={"cols": 20, "rows": 3}),}


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content",)
