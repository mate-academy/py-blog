from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("owner", "title", "content",)

        widgets = {
            "owner": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("owner", "title", "content",)

        widgets = {
            "owner": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),

        }


class CommentaryCreateForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.Textarea(
            attrs={"cols": 200, "rows": 3, "style": "width: 100%"}
        )
    )
