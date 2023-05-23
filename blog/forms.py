from django.forms import ModelForm

from blog.models import Commentary


class CommentaryCreateForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "Comment",
        }
