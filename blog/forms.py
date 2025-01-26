from django import forms


class CommentaryForm(forms.Form):
   comment = forms.CharField(
       label="",
       widget=forms.Textarea(attrs={"rows": 3, "cols": 115, "placeholder": "Enter your comment here..."})
   )
