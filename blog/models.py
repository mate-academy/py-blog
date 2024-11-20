from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return (f"{self.username}: "
                f"({self.email} {self.first_name} {self.last_name})")


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts")
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1500, default="need message")
    created_time = models.CharField(max_length=63)

    def get_absolute_url(self):
        return reverse("blog:post-list")

    def __str__(self):
        return f"{self.title} {self.created_time}"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries")
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries")
    created_time = models.CharField(max_length=63)
    content = models.CharField(max_length=1500, default="need message")

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.post.id})

    def __str__(self):
        return f"{self.content} {self.created_time}"
