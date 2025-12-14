from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system.settings import AUTH_USER_MODEL


class User(AbstractUser):

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name}) "


class Post(models.Model):
    owner = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.title} (written by {self.owner.username})"


class Commentary(models.Model):
    user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return (
            f"{self.user.username}"
            f" at {self.created_time.strftime('%d %b %Y, %H:%M')}"
        )
