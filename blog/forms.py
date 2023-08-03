from django import forms


class CommentaryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="")
    post_id = forms.IntegerField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput())
