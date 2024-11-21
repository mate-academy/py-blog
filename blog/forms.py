from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm

from blog.models import Commentary


class CommentaryForm(LoginRequiredMixin, ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {
            "content": "Add new comment"
        }
