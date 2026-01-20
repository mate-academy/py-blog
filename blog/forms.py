from django import forms
from django.forms import Textarea
from django.utils.translation import gettext_lazy

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(
        max_length=1023,
        widget=forms.Textarea(attrs={"rows": 3}),
        label=""
    )

    class Meta:
        model = Commentary
        fields = ["content"]
