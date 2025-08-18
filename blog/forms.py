from django.forms import ModelForm, Textarea

from blog.models import Commentary


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {"content": Textarea}
