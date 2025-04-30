from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.TextField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} by {self.owner.username}"


class Commentary(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return f"Comment by {self.user.username} on '{self.post.title}'"
