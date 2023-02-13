from django import forms

from blog.models import Commentary


class CommentaryFrom(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentaryFrom, self).__init__(*args, **kwargs)
        self.fields["content"].label = "Comment"

    class Meta:
        model = Commentary
        fields = ["content", ]
        widgets = {
            "content": forms.Textarea(attrs={"cols": "100", "rows": "5"})
        }
