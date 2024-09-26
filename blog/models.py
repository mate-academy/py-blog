from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self):
        return f"{self.title} [{self.created_time}]"


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"

    def __str__(self):
        return f"Comment for {self.post} ({self.created_time})"
