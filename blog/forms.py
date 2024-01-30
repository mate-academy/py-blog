from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from blog.models import Commentary


class CreateCommentary(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content", "post"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "cols": 60, "class": "form-control"}
            ),
            "post": forms.TextInput(attrs={"style": "display:none"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "align": "center",
                "placeholder": "set your password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "align": "center",
                "placeholder": "confirm your password",
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "create username"
                }
            )
        }
