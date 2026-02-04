from django.forms import ModelForm
from .models import Commentary


class CommentForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
