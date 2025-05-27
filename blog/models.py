from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        ordering = ("username",)


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="post"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=350)

    class Meta:
        ordering = ("-created_time",)
