from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import User, Commentary


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
