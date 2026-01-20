from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return f'{self.user.username}: "{self.content}"'
