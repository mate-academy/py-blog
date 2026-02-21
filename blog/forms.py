from django.forms import ModelForm

from blog.models import Commentary


class FormCommentary(ModelForm):
    class Meta:
        model = Commentary
        fields = ["content", "user", "post"]