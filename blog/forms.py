from crispy_forms.helper import FormHelper
from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ["content"]
