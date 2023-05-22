from django.contrib.auth.forms import UserCreationForm
from blog.models import Post, User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name")
