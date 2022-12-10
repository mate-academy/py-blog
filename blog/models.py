from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ["first_name"]


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, related_name="commentaries", on_delete=models.CASCADE
    )
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Commentaries"
