from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, Group
from django.contrib import admin
from django.test import TestCase
from django.urls import reverse

from blog.forms import CommentaryForm
from blog.models import Commentary, Post


class CommentTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="reader", password="test-password"
        )
        self.other = get_user_model().objects.create_user(username="other")
        self.post = Post.objects.create(
            owner=self.other, title="A story", content="Story content"
        )
        self.url = self.post.get_absolute_url()

    def test_anonymous_comment_is_invalid(self):
        form = CommentaryForm(
            data={"content": "Hello"}, user=AnonymousUser()
        )
        self.assertFalse(form.is_valid())
        response = self.client.post(self.url, {"content": "Hello"})
        self.assertContains(response, "Please log in")
        self.assertFalse(Commentary.objects.exists())

    def test_authenticated_comment_uses_request_user_and_current_post(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, {
            "content": "Hello", "user": self.other.pk, "post": 999
        })
        self.assertRedirects(response, self.url)
        comment = Commentary.objects.get()
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.content, "Hello")
        self.assertContains(self.client.get(self.url), "Hello")

    def test_blank_comment_is_rejected(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, {"content": "   "})
        self.assertContains(response, "This field is required")
        self.assertFalse(Commentary.objects.exists())

    def test_detail_only_displays_its_own_comments_and_escapes_content(self):
        other_post = Post.objects.create(
            owner=self.user, title="Other", content="Other story"
        )
        Commentary.objects.create(
            post=other_post, user=self.user, content="Unrelated comment"
        )
        Commentary.objects.create(
            post=self.post, user=self.user, content="<script>alert(1)</script>"
        )
        response = self.client.get(self.url)
        self.assertNotContains(response, "Unrelated comment")
        self.assertContains(response, "&lt;script&gt;")

    def test_missing_post_returns_404(self):
        url = reverse("blog:post-detail", args=[999])
        self.assertEqual(self.client.get(url).status_code, 404)
        self.assertEqual(self.client.post(url, {"content": "Hi"}).status_code, 404)

    def test_login_and_logout(self):
        response = self.client.post(reverse("login"), {
            "username": "reader", "password": "test-password", "next": self.url
        })
        self.assertRedirects(response, self.url)
        self.assertContains(self.client.get(self.url), "Post comment")
        self.assertRedirects(
            self.client.post(reverse("logout")), reverse("blog:index")
        )

    def test_group_is_not_registered(self):
        self.assertNotIn(Group, admin.site._registry)
