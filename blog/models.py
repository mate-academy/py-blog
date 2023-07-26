from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    created_time = models.DateTimeField()

    class Meta:
        ordering = ["created_time"]

    def __str__(self) -> str:
        return f"{self.owner} - {self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField()
    content = models.TextField(max_length=500)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return f"{self.user}"
