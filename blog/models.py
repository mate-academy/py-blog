from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="post", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comment",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="comment",
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "commentaries"
        ordering = ["-created_time"]
