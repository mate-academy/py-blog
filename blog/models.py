from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    owner = models.ForeignKey(
        "blog.User", on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"


class Commentary(models.Model):
    user = models.ForeignKey(
        "blog.User", on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
