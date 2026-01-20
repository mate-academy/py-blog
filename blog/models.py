from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "commentaries"

    def __str__(self):
        return f"Commentary to post:  {self.post.title}"
