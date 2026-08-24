from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Commentary, Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="alice",
            password="secret123"
        )

    def test_index_orders_posts_by_created_time_desc(self):
        Post.objects.create(
            title="Older",
            content="old content",
            owner=self.user,
        )
        Post.objects.create(
            title="Newer",
            content="new content",
            owner=self.user,
        )

        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.context["post_list"][0].title, "Newer")

    def test_index_has_five_posts_per_page(self):
        for i in range(12):
            Post.objects.create(
                title=f"Post {i}",
                content=f"Content {i}",
                owner=self.user,
            )

        response = self.client.get(reverse("blog:index"))
        self.assertEqual(len(response.context["post_list"]), 5)

    def test_anonymous_user_cannot_post_comment(self):
        post = Post.objects.create(
            title="Example",
            content="Some text",
            owner=self.user,
        )
        response = self.client.post(
            reverse("blog:post-detail", args=[post.pk]),
            {"content": "Hello"},
            follow=True,
        )
        self.assertContains(
            response, "You must be logged in to post a comment."
        )

    def test_authenticated_user_can_post_comment(self):
        post = Post.objects.create(
            title="Example",
            content="Some text",
            owner=self.user,
        )
        self.client.login(username="alice", password="secret123")

        self.client.post(
            reverse("blog:post-detail", args=[post.pk]),
            {"content": "Comment from user"},
            follow=True,
        )

        self.assertTrue(Commentary.objects.filter(
            post=post,
            user=self.user,
            content="Comment from user"
        ).exists())
