from django import forms


class CommentaryForm(forms.Form):
    content = forms.CharField(required=True)
