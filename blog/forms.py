from django import forms
from django.forms import Textarea
from django.utils.translation import gettext_lazy

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": gettext_lazy("Commentary")}
