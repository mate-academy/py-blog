from django.db import models

from django.contrib.auth.models import AbstractUser

from blog_system import settings


class User(AbstractUser):

    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "comments"
