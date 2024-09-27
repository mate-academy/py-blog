from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ("username",)


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts_owned",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="related_posts")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
