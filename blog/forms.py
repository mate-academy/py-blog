from django import forms
from .models import Commentary
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ('content',) # Дозволяємо користувачу вводити лише контент коментаря

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Add a comment', css_class='btn-primary'))
        self.helper.form_method = 'post'