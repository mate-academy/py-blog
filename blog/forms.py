from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = (
            "content",
            "user",
            "post",
        )

    def __init__(self, *args, **kwargs):
        super(CommentaryForm, self).__init__(*args, **kwargs)
        self.fields["user"].widget = forms.HiddenInput()
        self.fields["post"].widget = forms.HiddenInput()
