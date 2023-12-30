from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Commentary


class CommentaryCreateForm(LoginRequiredMixin, forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 3, "placeholder": "Write your comment here..."}
        ),
        label=""
    )

    class Meta:
        model = Commentary
        fields = ("content", )
