from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
    )
    owner = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
        null=True,
    )

    class Meta:
        ordering = ["-created_time"]
