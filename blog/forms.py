from django import forms
from django.contrib.auth.models import AnonymousUser

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Share your thoughts...",
                    "rows": 4,
                }
            )
        }

    def __init__(
        self,
        *args: object,
        user: object | None = None,
        **kwargs: object,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.user = user or AnonymousUser()

    def clean(self) -> dict[str, object]:
        cleaned_data = super().clean()
        if not getattr(self.user, "is_authenticated", False):
            raise forms.ValidationError(
                "You must be logged in to leave a comment."
            )
        return cleaned_data
