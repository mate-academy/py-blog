from django import forms
from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Customize form widgets or add CSS classes
        self.fields["content"].widget.attrs.update({"class": "form-control", "placeholder": "Enter your comment here"})