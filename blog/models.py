from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_time",)

    def __str__(self):
        return (
            f"Post {self.title} "
            f"Created by: {self.owner} "
            f"At: {self.created_time})"
        )


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="commentaries",
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ("created_time",)

    def __str__(self):
        return (
            f"{self.user} commented post "
            f"Post id: {self.post.pk} "
            f"At: {self.created_time})"
        )
