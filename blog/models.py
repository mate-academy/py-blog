from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_time"]
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "title"],
                name="unique_title")
        ]


class Commentary(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    class Meta:
        ordering = ["-created_time"]


class User(AbstractUser):
    pass
