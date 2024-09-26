from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ["created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        name="user",
        related_name="commentaries"
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        name="post",
        related_name="commentaries"
    )

    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
