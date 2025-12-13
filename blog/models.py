from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
