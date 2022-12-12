class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
