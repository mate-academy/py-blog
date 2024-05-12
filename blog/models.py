from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "commentaries"
