from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        related_name="posts",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="commentaries", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="commentaries", on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
