from django import forms


class CommentaryCreate(forms.Form):
    content = forms.TextInput()
