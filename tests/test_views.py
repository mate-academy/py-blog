from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Commentary

MAIN_PAGE_URL = reverse("blog:index")
PAGINATION = 5


class PostListTest(TestCase):
    fixtures = [
        "blog_system_db_data.json",
    ]

    def test_main_page_(self):
        response = self.client.get(MAIN_PAGE_URL)

        self.assertEqual(response.status_code, 200)

    def test_main_page_paginated_correctly(self):
        response = self.client.get(MAIN_PAGE_URL)

        self.assertEqual(
            len(response.context["post_list"]), PAGINATION
        )

    def test_main_page_ordered_by_created_time(self):
        response = self.client.get(MAIN_PAGE_URL)
        post_list = Post.objects.all().order_by("-created_time")
        post_context = response.context["post_list"]

        self.assertEqual(
            list(post_context),
            list(post_list[: len(post_context)]),
        )

    def test_main_page_second_page_and_navigation(self):
        owner = Post.objects.first().owner
        for index in range(PAGINATION + 1):
            Post.objects.create(
                owner=owner,
                title=f"Additional post {index}",
                content="Additional content",
            )

        response = self.client.get(MAIN_PAGE_URL, {"page": 2})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page_obj"].number, 2)
        self.assertTrue(response.context["page_obj"].has_previous())
        self.assertContains(response, "Previous")

    def test_main_page_displays_post_author_and_comment_count(self):
        post = Post.objects.first()
        Commentary.objects.create(
            user=post.owner,
            post=post,
            content="A countable comment",
        )

        response = self.client.get(MAIN_PAGE_URL)
        displayed_post = next(
            item for item in response.context["post_list"] if item.pk == post.pk
        )

        self.assertContains(response, post.owner.username)
        self.assertContains(response, f"Comments: {post.commentaries.count()}")
        self.assertEqual(displayed_post.comment_count, post.commentaries.count())


class PostDetailTest(TestCase):
    fixtures = [
        "blog_system_db_data.json",
    ]

    def test_post_detail_response_with_correct_template(self):
        response = self.client.get(reverse("blog:post-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")

    def test_post_detail_url_uses_posts_path(self):
        self.assertEqual(reverse("blog:post-detail", args=[1]), "/posts/1/")

    def test_post_detail_displays_post_comments(self):
        post = Post.objects.get(pk=1)
        commentary = Commentary.objects.create(
            user=post.owner,
            post=post,
            content="A visible comment",
        )

        response = self.client.get(reverse("blog:post-detail", args=[post.pk]))

        self.assertContains(response, commentary.content)

    def test_anonymous_user_cannot_create_comment(self):
        response = self.client.post(
            reverse("blog:post-detail", args=[1]),
            {"content": "Anonymous comment"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["form"].is_valid())
        self.assertFalse(Commentary.objects.filter(content="Anonymous comment").exists())

    def test_authenticated_user_can_create_comment(self):
        user = get_user_model().objects.create_user(
            username="commenter",
            password="test-password",
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse("blog:post-detail", args=[1]),
            {"content": "Authenticated comment"},
        )

        self.assertRedirects(response, reverse("blog:post-detail", args=[1]))
        self.assertTrue(
            Commentary.objects.filter(
                post_id=1,
                user=user,
                content="Authenticated comment",
            ).exists()
        )

