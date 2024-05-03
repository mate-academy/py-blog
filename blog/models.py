from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "comments"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
