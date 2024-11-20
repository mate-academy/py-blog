from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentaryForm, self).__init__(*args, **kwargs)
        self.fields[
            "content"
        ].widget.attrs[
            "style"
        ] = "resize: none; width: 100%; height: 20vh;"

    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {"content": "Add a new comment"}
