from django.forms import ModelForm

from blog.models import Commentary


class CommentaryModelForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
