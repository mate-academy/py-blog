from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        default_related_name = "users"
        verbose_name = "user"
        verbose_name_plural = "users"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = "posts"

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        default_related_name = "comments"
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"
