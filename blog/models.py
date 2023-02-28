from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        ordering = ["username"]


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["owner"]

    def __str__(self) -> str:
        return (
            f"{self.owner} add '{self.title}'"
            f" at ({self.created_time.strftime('%d-%m-%Y %H:%M:%S')})"
        )


class Commentary(models.Model):
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
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default=":-)")

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return (
            f"{self.user} comments "
            f"{self.post.title} at "
            f"({self.created_time.strftime('%d-%m-%Y %H:%M:%S')})"
        )
