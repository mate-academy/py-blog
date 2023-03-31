from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ["username"]


class Post(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(
        max_length=64
    )
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries",
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.CharField(max_length=64)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "commentaries"
        ordering = ["created_time"]

    def __str__(self):
        return self.content
