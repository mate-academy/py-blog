from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Commentary
from .forms import CommentaryForm

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
            email="test@example.com",
            first_name="Test",
            last_name="User"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("testpass123"))


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            owner=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "Test Content")
        self.assertEqual(self.post.owner, self.user)

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")


class CommentaryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            owner=self.user
        )
        self.commentary = Commentary.objects.create(
            content="Test Comment",
            user=self.user,
            post=self.post
        )

    def test_commentary_creation(self):
        self.assertEqual(self.commentary.content, "Test Comment")
        self.assertEqual(self.commentary.user, self.user)
        self.assertEqual(self.commentary.post, self.post)

    def test_commentary_str(self):
        expected_str = f"{self.user.username}'s comment on {self.post.title}"
        self.assertEqual(str(self.commentary), expected_str)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            owner=self.user
        )

    def test_index_view(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(
            reverse("blog:post-detail", kwargs={"pk": self.post.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")
        self.assertContains(response, "Test Post")
        self.assertContains(response, "Test Content")

    def test_post_detail_view_with_comment(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("blog:post-detail", kwargs={"pk": self.post.pk}),
            {"content": "New Comment"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Commentary.objects.filter(
                content="New Comment",
                user=self.user,
                post=self.post
            ).exists()
        )


class CommentaryFormTest(TestCase):
    def test_commentary_form_valid(self):
        form_data = {"content": "Test Comment"}
        form = CommentaryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_commentary_form_empty(self):
        form_data = {"content": ""}
        form = CommentaryForm(data=form_data)
        self.assertFalse(form.is_valid())
