from django.test import TestCase
from blog.models import Post, Commentary
from django.contrib.auth import get_user_model

User = get_user_model()


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="User1", password="Password1"
        )
        self.post = Post.objects.create(
            title="Title1", content="Body1", owner=self.user
        )

    def test_post_str(self):
        self.assertEqual(self.post.__str__(), "Title1")


class CommentaryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="User1", password="Password1"
        )
        self.post = Post.objects.create(
            title="Title1", content="Body1", owner=self.user
        )
        self.commentary = Commentary.objects.create(
            content="BodyCommentary1", user=self.user, post=self.post
        )

    def test_commentary_str(self):
        self.assertEqual(self.commentary.__str__(), "BodyCommentary1")
