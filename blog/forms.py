from django import forms

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Write your comment here...",
                    "rows": 5}
            ),
        }

    def __init__(self, *args, **kwargs):
        # Allow an external error message to be passed to the form
        self.user_is_authenticated = kwargs.pop('user_is_authenticated', True)
        super().__init__(*args, **kwargs)

        if not self.user_is_authenticated:
            self.add_error(None, "You must be logged in to add a comment.")