from django.test import TestCase
from blog.forms import CommentaryForm
from django.contrib.auth import get_user_model
from blog.models import Post

User = get_user_model()


class CommentaryFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.post = Post.objects.create(
            title="Test Post", content="Lorem ipsum", owner=self.user
        )

    def test_commentary_form_valid(self):
        form_data = {"content": "Nice post!"}
        form = CommentaryForm(data=form_data, user=self.user, post=self.post)
        self.assertTrue(form.is_valid())

    def test_commentary_form_empty_content(self):
        form_data = {"content": ""}
        form = CommentaryForm(data=form_data, user=self.user, post=self.post)
        self.assertFalse(form.is_valid())

    def test_only_logged_in_users_can_add_commentary(self):
        form_data = {"content": "Nice post!"}
        form = CommentaryForm(data=form_data, user=None, post=self.post)
        self.assertFalse(form.is_valid())
