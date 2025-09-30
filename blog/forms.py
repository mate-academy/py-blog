from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {
            'content': 'Write your comment here',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Type your comment...',
            'class': 'form-control',
            'rows': 4,
        })