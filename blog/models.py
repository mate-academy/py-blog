from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_time = models.CharField(max_length=256)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.title}  {self.content}"


class Commentary(models.Model):
    created_time = models.CharField(max_length=256)
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )

    class Meta:
        ordering = ("created_time",)

    def __str__(self):
        return f"{self.content} created at {self.created_time} by {self.user}"
