from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system.settings import AUTH_USER_MODEL


class User(AbstractUser):
    class Meta:
        ordering = ["username"]


class Post(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner"
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = [
            "-created_time",
        ]


class Commentary(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "commentaries"
        ordering = [
            "-created_time",
        ]
