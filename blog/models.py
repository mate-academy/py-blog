from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


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
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self) -> str:
        return f"Commentary dated the {self.created_time}"

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"
