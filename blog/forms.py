from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from blog.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field(
                "content",
                rows="3",
                placeholder="Write your comment here..."
            ),
        )
        self.helper.add_input(Submit(
            "submit", "Add comment", css_class="btn-primary mt-2"
        ))
