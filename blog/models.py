from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
