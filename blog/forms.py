from django.contrib.auth.forms import UserCreationForm
from blog.models import User, Commentary
from django import forms


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "username",
            "email",
            "password1",
            "password2",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"placeholder": "Add a comment..."}
            ),
        }
