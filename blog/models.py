from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        ordering = ["username"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blogs"
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"
