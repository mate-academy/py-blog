from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Post: {self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self) -> str:
        return f"Commentary: {self.content}"
