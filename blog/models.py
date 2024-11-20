from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    class Meta:
        ordering = ("title",)

    def __str__(self) -> str:
        return (f"{self.title} ({self.owner} "
                f"{self.created_time.strftime('%m-%d-%Y %H:%M')})")


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(
        max_length=255,
        help_text="Enter comment content"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
