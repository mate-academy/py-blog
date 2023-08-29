from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        required=False,
        queryset=get_user_model().objects.all(),
        widget=forms.HiddenInput
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5}),
        label="Share your thoughts"
    )

    class Meta:
        model = Commentary
        fields = "__all__"
        widgets = {"post": forms.HiddenInput}

    def clean(self):
        user = self.cleaned_data.get("user", None)
        if not user:
            raise ValidationError("Please log in to post comments.")

        return self.cleaned_data
