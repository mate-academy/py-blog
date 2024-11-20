from datetime import datetime

from django import forms

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    post_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    user_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Commentary
        fields = ["content", ]
