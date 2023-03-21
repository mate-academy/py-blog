from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import Commentary, User


class PostSearchForm(forms.Form):
    description = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )


class CommentaryForm(forms.Form):
    class Meta:
        model = Commentary
        fields = "__all__"


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )
