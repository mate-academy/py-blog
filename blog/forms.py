from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import User, Commentary


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", required=True, widget=forms.Textarea())

    class Meta:
        model = Commentary
        fields = ["content"]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
