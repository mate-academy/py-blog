from django.forms import ModelForm

from blog.models import Commentary


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
