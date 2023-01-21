from django import forms

from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["post"].empty_label = "Категорія не вибрана"

    class Meta:
        model = Commentary
        fields = ["content"]
        # fields = "__all__"
        labels = {"content": "Add your comment:"}
        # widgets = {
        #     "content": forms.Textarea(attrs={"cols": 10, "rows": 15})
        # }
