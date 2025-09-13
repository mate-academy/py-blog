from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.title}: ({self.created_time})"


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")

    class Meta:
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.content}: ({self.created_time})"
