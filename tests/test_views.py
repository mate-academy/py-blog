from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment

MAIN_PAGE_URL = reverse("blog:index")
PAGINATION = 5


class PostListTest(TestCase):
    fixtures = ["blog_system_db_data.json"]

    def test_main_page_status_code(self):
        response = self.client.get(MAIN_PAGE_URL)
        self.assertEqual(response.status_code, 200)

    def test_main_page_paginated_correctly(self):
        response = self.client.get(MAIN_PAGE_URL)
        self.assertEqual(len(response.context["page_obj"]), PAGINATION)

    def test_main_page_ordered_by_created_time(self):
        response = self.client.get(MAIN_PAGE_URL)
        expected_posts = list(Post.objects.order_by("-created_time")[:PAGINATION])
        actual_posts = list(response.context["page_obj"])
        self.assertEqual(actual_posts, expected_posts)


class PostDetailTest(TestCase):
    fixtures = ["blog_system_db_data.json"]

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_post_detail_response_with_correct_template(self):
        response = self.client.get(reverse("blog:post-detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
