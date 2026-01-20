from django.db import models
from django.contrib.auth.models import AbstractUser

from blog_system import settings


class User(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=63)
    content = models.CharField(max_length=63)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_time"].reverse()

    def __str__(self):
        return f"{self.owner} - {self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.user} - {self.post} - {self.created_time}"
