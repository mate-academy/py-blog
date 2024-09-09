from django import forms
from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget = forms.Textarea(attrs={
            "rows": 2,
            "cols": 50,
        })
        self.fields["content"].label = ""
