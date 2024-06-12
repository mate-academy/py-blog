from django.forms import ModelForm, Textarea

from .models import Commentary


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": Textarea(attrs={
                "class": "border",
                "style": "color: white",
                "rows": 3,
                "cols": 126,
            })
        }
