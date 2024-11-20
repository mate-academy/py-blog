from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


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
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=300)
    created_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=200)

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"
        ordering = ["-created_time"]
