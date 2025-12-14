from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("blog:index")


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ["-created_time"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["created_time"]),
        ]

    def __str__(self):
        return f"{self.title} ({self.owner.username})"


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.user.username} write:"
