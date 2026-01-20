from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name_plural = "Users"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1500)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.owner} created: {self.created_time}"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1500)

    class Meta:
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return f"{self.user} {self.content}"
