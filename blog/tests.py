from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse

from blog.forms import CommentaryForm
from blog.models import Commentary, Post

User = get_user_model()


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="john.doe",
            first_name="John",
            last_name="Doe",
            password="securepassword123",
        )
        self.post = Post.objects.create(
            owner=self.user,
            title="Django Testing",
            content="Testing is essential for quality software.",
        )
        self.commentary = Commentary.objects.create(
            user=self.user,
            post=self.post,
            content="Informative article!",
        )

    def test_user_str(self):
        self.assertEqual(str(self.user), "john.doe: (John Doe)")

    def test_post_str(self):
        self.assertEqual(str(self.post), f"Django Testing ({self.user})")

    def test_commentary_str(self):
        self.assertEqual(
            str(self.commentary), f"{self.user}: ({self.post})"
        )


class CommentaryFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="commenter",
            password="securepassword123",
        )

    def test_form_valid_with_authenticated_user(self):
        form_data = {"content": "Valid comment"}
        form = CommentaryForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_form_invalid_with_anonymous_user(self):
        form_data = {"content": "Anonymous attempt"}
        form = CommentaryForm(data=form_data, user=AnonymousUser())
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)

    def test_form_invalid_without_user(self):
        form_data = {"content": "Missing user"}
        form = CommentaryForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)

    def test_form_content_is_required(self):
        form_data = {"content": ""}
        form = CommentaryForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)


class PostViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="author",
            password="securepassword123",
        )
        # Створюємо кілька постів для перевірки сортування
        self.posts = [
            Post.objects.create(
                owner=self.user,
                title=f"Post #{i}",
                content=f"Content for post #{i}",
            )
            for i in range(1, 8)
        ]
        self.first_post = self.posts[0]

    def test_index_page_status_code_and_template(self):
        url = reverse("blog:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_main_page_ordered_by_created_time(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        post_list = Post.objects.all().order_by("-created_time")
        post_context = response.context["post_list"]

        self.assertEqual(
            list(post_context),
            list(post_list[: len(post_context)]),
        )

    def test_post_detail_url_uses_posts_prefix(self):
        url = reverse("blog:post-detail", args=[self.first_post.pk])
        self.assertTrue(url.endswith(f"/posts/{self.first_post.pk}/"))

    def test_post_detail_response_with_correct_template(self):
        url = reverse("blog:post-detail", args=[self.first_post.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")
        self.assertEqual(response.context["post"], self.first_post)

    def test_post_detail_displays_existing_comments(self):
        comment = Commentary.objects.create(
            user=self.user,
            post=self.first_post,
            content="Sample comment for display",
        )
        url = reverse("blog:post-detail", args=[self.first_post.pk])
        response = self.client.get(url)

        self.assertContains(response, comment.content)
        self.assertContains(response, self.user.username)

    def test_authenticated_user_can_create_comment(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", args=[self.first_post.pk])
        form_data = {"content": "Brand new comment via POST"}

        response = self.client.post(url, data=form_data)

        # Очікується редирект на ту саму сторінку після успішного створення
        self.assertRedirects(response, url)
        self.assertTrue(
            Commentary.objects.filter(
                content="Brand new comment via POST",
                user=self.user,
                post=self.first_post,
            ).exists()
        )

    def test_unauthenticated_user_cannot_create_comment(self):
        url = reverse("blog:post-detail", args=[self.first_post.pk])
        form_data = {"content": "Malicious anonymous comment"}

        self.client.post(url, data=form_data)

        self.assertFalse(
            Commentary.objects.filter(
                content="Malicious anonymous comment"
            ).exists()
        )
