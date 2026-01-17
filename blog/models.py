from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments")
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time"]
