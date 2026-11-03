from blog.models import Commentary

from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Commentary
        fields = [
            "content",
        ]
