from django import forms


class CommentaryForm(forms.Form):
    content = forms.CharField(max_length=255)
