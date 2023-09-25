from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )

    def __str__(self) -> str:
        return f"{self.created_time} {self.content}"
