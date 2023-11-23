from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    class Meta:
        ordering = ("username", )

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ("-created_time", )

    def __str__(self) -> str:
        return (f"owner:{self.owner},"
                f"title: {self.title},"
                f"created: {self.created_time}")


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="owners"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="posts")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ("-created_time", )

    def __str__(self) -> str:
        return f"user:{self.user}, created: {self.created_time}"
