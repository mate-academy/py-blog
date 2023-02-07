from django import forms

from blog.models import Commentary


# class CommentForm(forms.ModelForm):
#     content = forms.CharField(required=True)
#
#     class Meta:
#         model = Commentary
#         fields = ("content",)
