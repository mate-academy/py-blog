from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255, default="Untitled")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "comments"

    def __str__(self) -> str:
        return (
            f"Comment by {self.user.username} on {self.post.title}: "
            f"{self.content[:15]}..."
        )
