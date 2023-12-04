from django.forms import ModelForm

from blog.models import Commentary


class CommentForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ('content',)
        labels = {"content": ""}
