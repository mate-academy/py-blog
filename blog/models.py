from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        ordering = ("username", )


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.title}' by {self.owner}"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f"'{self.content[:32]}...' by {self.user}"

    class Meta:
        verbose_name_plural = "Commentaries"
