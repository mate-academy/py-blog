from django import forms
from django.forms import Textarea

from .models import *


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
