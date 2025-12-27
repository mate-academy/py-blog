from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from blog.forms import CommentaryForm
from blog.models import Post, Commentary
from blog.views import IndexView, PostDetailView


User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.post = Post.objects.create(
            title="Test Post",
            content="Test content",
            author=self.user,
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_commentaries_count(self):
        Commentary.objects.create(
            post=self.post,
            author=self.user,
            content="Test comment"
        )
        self.assertEqual(self.post.commentaries_count(), 1)


class CommentaryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.post = Post.objects.create(
            title="Test Post",
            content="Test content",
            author=self.user,
        )
        self.commentary = Commentary.objects.create(
            post=self.post,
            author=self.user,
            content="Hello!"
        )

    def test_commentary_str(self):
        self.assertEqual(
            str(self.commentary),
            f"Commentary by {self.user} on {self.post}"
        )


class CommentaryFormTest(TestCase):
    def test_form_valid_data(self):
        form = CommentaryForm(data={"content": "Nice post!"})
        self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        form = CommentaryForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)


class PostDetailCommentCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.post = Post.objects.create(
            title="Test",
            content="Content",
            author=self.user
        )

    def test_comment_created_when_logged_in(self):
        self.client.login(username="user", password="pass")
        response = self.client.post(
            reverse("blog:post-detail", args=[self.post.pk]),
            data={"content": "New comment"}
        )
        self.assertEqual(Commentary.objects.count(), 1)
        self.assertEqual(response.status_code, 302)

    def test_comment_not_created_when_anonymous(self):
        response = self.client.post(
            reverse("blog:post-detail", args=[self.post.pk]),
            data={"content": "New comment"}
        )
        self.assertEqual(Commentary.objects.count(), 0)
        self.assertEqual(response.status_code, 200)


class BlogURLTests(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("blog:index")
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_post_detail_url_resolves(self):
        url = reverse("blog:post-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)


class CommentPermissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.post = Post.objects.create(
            title="Test",
            content="Content",
            author=self.user
        )

    def test_anonymous_user_cannot_comment(self):
        self.client.post(
            reverse("blog:post-detail", args=[self.post.pk]),
            data={"content": "Hello"}
        )
        self.assertEqual(Commentary.objects.count(), 0)

    def test_logged_in_user_can_comment(self):
        self.client.login(username="user", password="pass")
        self.client.post(
            reverse("blog:post-detail", args=[self.post.pk]),
            data={"content": "Hello"}
        )
        self.assertEqual(Commentary.objects.count(), 1)
