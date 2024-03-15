from django.test import TestCase
from django.urls import reverse
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

        self.assertEqual(len(response.context["post_list"]), PAGINATION)

    def test_main_page_ordered_by_created_time(self):
        response = self.client.get(MAIN_PAGE_URL)
        post_list = Post.objects.all().order_by("-created_time")
        post_context = response.context["post_list"]

        self.assertEqual(
            list(post_context),
            list(post_list[: len(post_context)]),
        )


class PostDetailTest(TestCase):
    fixtures = [
        "blog_system_db_data.json",
    ]

    def test_post_detail_response_with_sorrect_template(self):
        response = self.client.get(reverse("blog:post-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")
