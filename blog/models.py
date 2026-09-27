from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Blog account able to own posts and leave commentaries."""

    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        full_name = self.get_full_name()
        if full_name:
            return f"{full_name} (@{self.username})"
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self) -> str:
        return f"{self.title} — by {self.owner}"


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries",
    )

    class Meta:
        ordering = ["created_time"]
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return f"Commentary by {self.user} on “{self.post}”"
