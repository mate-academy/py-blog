from django import forms

from blog.models import Commentary


class CommentForm(forms.Form):
    model = Commentary
    fields = ["content", "user_id", "post_id"]
