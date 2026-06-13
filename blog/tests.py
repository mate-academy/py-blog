from django.test import TestCase
from django.urls import reverse
from blog.models import User, Post, Commentary


class UserModelTest(TestCase):
    def test_user_str(self):
        user = User(username="testuser", email="test@test.com")
        self.assertEqual(str(user), "testuser")


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass123"
        )

    def test_post_creation(self):
        post = Post.objects.create(
            owner=self.user, title="Test Post", content="Test content"
        )
        self.assertEqual(str(post), "Test Post")
        self.assertEqual(post.owner, self.user)

    def test_post_ordering(self):
        Post.objects.create(
            owner=self.user,
            title="Post 1",
            content="Content 1"
        )
        post2 = Post.objects.create(
            owner=self.user, title="Post 2", content="Content 2"
        )
        posts = Post.objects.all()
        self.assertEqual(posts[0], post2)


class CommentaryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass123"
        )
        self.post = Post.objects.create(
            owner=self.user, title="Test Post", content="Test content"
        )

    def test_commentary_creation(self):
        comment = Commentary.objects.create(
            user=self.user, post=self.post, content="Test comment"
        )
        self.assertEqual(str(comment), "commented by testuser")


class IndexViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass123"
        )
        for i in range(6):
            Post.objects.create(
                owner=self.user, title=f"Post {i}", content=f"Content {i}"
            )

    def test_index_view_status_code(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(len(response.context["page_obj"]), 5)


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass123"
        )
        self.post = Post.objects.create(
            owner=self.user, title="Test Post", content="Test content"
        )

    def test_detail_view_status_code(self):
        response = self.client.get(
            reverse("blog:post-detail", kwargs={"pk": self.post.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_comment_form_present_for_authenticated_user(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(
            reverse("blog:post-detail", kwargs={"pk": self.post.pk})
        )
        self.assertIn("commentary_form", response.context)

    def test_comment_form_not_for_anonymous(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.pk})
        response = self.client.get(url)
        self.assertNotIn("commentary_form", response.context)


class CommentaryFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass123"
        )
        self.post = Post.objects.create(
            owner=self.user, title="Test Post", content="Test content"
        )

    def test_comment_creation(self):
        self.client.login(username="testuser", password="testpass123")
        self.client.post(
            reverse("blog:post-detail", kwargs={"pk": self.post.pk}),
            {"content": "New comment"},
        )
        self.assertEqual(Commentary.objects.count(), 1)

    def test_anonymous_cannot_comment(self):
        self.client.post(
            reverse("blog:post-detail", kwargs={"pk": self.post.pk}),
            {"content": "New comment"},
        )
        self.assertEqual(Commentary.objects.count(), 0)
