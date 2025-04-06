from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import Commentary, User


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({"class": "form-control"})


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ("username", "email")
