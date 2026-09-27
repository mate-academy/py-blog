from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    """Commentary creation form.

    The form itself rejects anonymous submitters, so even a crafted
    POST request from a logged-out user cannot create a commentary.
    """

    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": "Your commentary"}
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Share your thoughts about this post…",
                }
            ),
        }

    def __init__(self, *args, request_user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.request_user = request_user

    def clean(self):
        cleaned_data = super().clean()
        user = self.request_user
        if user is None or not user.is_authenticated:
            raise forms.ValidationError(
                "Only signed-in users may leave commentaries. "
                "Please log in and try again."
            )
        return cleaned_data
