from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": 4})}

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        if not self.user or not self.user.is_authenticated:
            raise forms.ValidationError("Please log in to leave a comment.")
        return cleaned_data
