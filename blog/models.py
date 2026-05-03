from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return (
            f"{self.username} ({full_name})"
            if full_name else self.username
        )


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self) -> str:
        _date = datetime.strftime(
            self.created_time,
            "%d-%m-%Y %H:%M:%S"
        )
        return (
            f"{self.title} | "
            f"{self.owner.username} | "
            f"{_date}"
        )


class Commentary(models.Model):
    content = models.TextField(blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return f"'{self.content}' (created by: {self.user.username})"
