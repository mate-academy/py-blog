from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=255)
    post = models.ForeignKey(
        Post,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
