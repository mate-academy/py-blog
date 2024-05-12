from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    """Made to be a mixin in PostDetailView to add detailed view of comments"""

    class Meta:
        model = Commentary
        fields = [
            "content",
        ]
