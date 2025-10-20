from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Wpisz swój komentarz tutaj...'}),
        }