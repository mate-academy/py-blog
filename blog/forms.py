from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Commentary
        fields = ('content',)
