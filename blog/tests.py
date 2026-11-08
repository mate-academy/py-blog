from django.test import TestCase
from django.urls import reverse

from blog.forms import CommentaryForm
from blog.models import Commentary, Post, User


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="author", password="pass12345"
        )
        self.posts = [
            Post.objects.create(
                owner=self.user, title=f"Post {i}", content=f"Content {i}"
            )
            for i in range(7)
        ]


class IndexViewTests(BaseTestCase):
    def test_index_status_and_template(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_pagination_five_per_page(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(len(response.context["post_list"]), 5)
        response = self.client.get(reverse("blog:index") + "?page=2")
        self.assertEqual(len(response.context["post_list"]), 2)

    def test_posts_ordered_by_created_time_desc(self):
        response = self.client.get(reverse("blog:index"))
        times = [p.created_time for p in response.context["post_list"]]
        self.assertEqual(times, sorted(times, reverse=True))

    def test_comments_count_displayed(self):
        post = self.posts[-1]
        Commentary.objects.create(user=self.user, post=post, content="Hi")
        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "1 comment")


class PostDetailViewTests(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.post = self.posts[0]
        self.url = reverse("blog:post-detail", kwargs={"pk": self.post.pk})

    def test_detail_page_shows_post_and_comments(self):
        Commentary.objects.create(
            user=self.user, post=self.post, content="Nice one"
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, "Nice one")

    def test_authenticated_user_can_comment(self):
        self.client.login(username="author", password="pass12345")
        response = self.client.post(self.url, {"content": "My comment"})
        self.assertRedirects(response, self.url)
        self.assertEqual(Commentary.objects.filter(post=self.post).count(), 1)

    def test_anonymous_user_cannot_comment(self):
        response = self.client.post(self.url, {"content": "Anon comment"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Commentary.objects.count(), 0)


class CommentaryFormTests(BaseTestCase):
    def test_form_invalid_for_anonymous_user(self):
        from django.contrib.auth.models import AnonymousUser

        form = CommentaryForm(
            {"content": "x"}, user=AnonymousUser(), post=self.posts[0]
        )
        self.assertFalse(form.is_valid())

    def test_form_valid_for_authenticated_user(self):
        form = CommentaryForm(
            {"content": "x"}, user=self.user, post=self.posts[0]
        )
        self.assertTrue(form.is_valid())
