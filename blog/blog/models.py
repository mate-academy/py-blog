from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(
        max_length=63
    )
    content = models.TextField()
    created_time = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return f"{self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(
        auto_now_add=True
    )
    content = models.TextField()

    class Meta:
        ordering = ["created_time"]
