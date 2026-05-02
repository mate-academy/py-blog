from django import forms

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {"content": ""}


class SearchForm(forms.Form):
    title = forms.CharField(label="",
                            max_length=255,
                            required=False,
                            widget=forms.TextInput(
                                attrs={"placeholder": "Search by title"})
                            )
