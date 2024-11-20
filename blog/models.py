from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self) -> str:
        return f"{self.user.username} ({self.created_time})"
