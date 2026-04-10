from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from django.shortcuts import reverse


from blog.admin import PostAdmin, CommentaryAdmin
from blog.models import Post, Commentary


class MockRequest:
    pass


class PostAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = PostAdmin(Post, self.site)

        self.user = get_user_model().objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.author = get_user_model().objects.create_user(
            username="Author1", password="password1"
        )
        self.author2 = get_user_model().objects.create_user(
            username="Author2", password="password2"
        )
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            title="Title1", content="Body1", owner=self.author
        )
        self.post2 = Post.objects.create(
            title="Title2", content="Body2", owner=self.author2
        )

        self.request = MockRequest()

    def test_admin_changelist_view(self):
        url = reverse("admin:blog_post_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title1")
        self.assertContains(response, "Author1")

    def test_admin_add_view(self):
        url = reverse("admin:blog_post_add")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_by_title(self):
        qs, _ = self.admin.get_search_results(
            self.request, Post.objects.all(), "Title1"
        )

        self.assertIn(self.post, qs)
        self.assertNotIn(self.post2, qs)

    def test_search_by_owner_username(self):
        qs, _ = self.admin.get_search_results(
            self.request, Post.objects.all(), "Author1"
        )

        self.assertIn(self.post, qs)
        self.assertNotIn(self.post2, qs)


class CommentaryAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = CommentaryAdmin(Commentary, self.site)

        self.user = get_user_model().objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.author = get_user_model().objects.create_user(
            username="Author1", password="password1"
        )
        self.post = Post.objects.create(
            title="Title1", content="Body1", owner=self.author
        )
        self.client.force_login(self.user)
        self.commentary = Commentary.objects.create(
            content="BodyCommentary1", user=self.author, post=self.post
        )
        self.commentary2 = Commentary.objects.create(
            content="BodyCommentary2", user=self.user, post=self.post
        )
        self.post_other = Post.objects.create(
            title="OtherPost", content="Other", owner=self.author
        )
        self.commentary_on_other_post = Commentary.objects.create(
            content="CommentOnOtherPost",
            user=self.author,
            post=self.post_other,
        )

        self.request = MockRequest()

    def test_admin_changelist_view(self):
        url = reverse("admin:blog_commentary_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BodyCommentary1")
        self.assertContains(response, "Author1")

    def test_admin_add_view(self):
        url = reverse("admin:blog_commentary_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_plural_name_displayed(self):
        url = reverse("admin:blog_commentary_changelist")
        response = self.client.get(url)
        self.assertContains(response, "Commentaries")

    def test_search_by_content(self):
        qs, _ = self.admin.get_search_results(
            self.request, Commentary.objects.all(), "BodyCommentary1"
        )

        self.assertIn(self.commentary, qs)
        self.assertNotIn(self.commentary2, qs)

    def test_search_by_owner_username(self):
        qs, _ = self.admin.get_search_results(
            self.request, Commentary.objects.all(), "Author1"
        )

        self.assertIn(self.commentary, qs)
        self.assertNotIn(self.commentary2, qs)

    def test_changelist_filter_by_user(self):
        url = reverse("admin:blog_commentary_changelist")
        response = self.client.get(
            url, {"user__id__exact": str(self.author.pk)}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BodyCommentary1")
        self.assertContains(response, "CommentOnOtherPost")
        self.assertNotContains(response, "BodyCommentary2")

    def test_changelist_filter_by_post(self):
        url = reverse("admin:blog_commentary_changelist")
        response = self.client.get(url, {"post__id__exact": str(self.post.pk)})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BodyCommentary1")
        self.assertContains(response, "BodyCommentary2")
        self.assertNotContains(response, "CommentOnOtherPost")
