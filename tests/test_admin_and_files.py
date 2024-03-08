import os
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteBlogTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user",
            password="testdata123456",
        )
        self.client.force_login(self.admin_user)

    def test_post_registered_in_admin(self):
        url = reverse("admin:blog_post_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_commentaries_registered_in_admin(self):
        url = reverse("admin:blog_commentary_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class GitignoreTests(TestCase):
    def test_gitignore_exist(self):
        file_exists = os.path.exists(".gitignore")
        assert file_exists

    def test_gitignore_has_correct_content(self):
        with open(".gitignore", "r") as gitignore:
            gitignore_content = gitignore.read()

            assert "idea" in gitignore_content
            assert "sqlite3" in gitignore_content
            assert "pyc" in gitignore_content


class IsStylesCSSExistTests(TestCase):
    def test_styles_exist(self):
        file_exists = os.path.exists("static/css/styles.css")

        self.assertTrue(file_exists)
