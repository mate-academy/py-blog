from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return f"{self.title} ({self.owner.username} {self.created_time})"


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentaries")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentaries")
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"
        ordering = ["-created_time"]
        indexes = [
            models.Index(fields=["post", "post"]),
        ]

    def __str__(self) -> str:
        return f"{self.created_time} ({self.user})"
