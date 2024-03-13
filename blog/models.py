from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):
    class Meta:
        ordering = ("username",)


class Post(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=255)

    def __str__(self):
        return f"Title: {self.title} with Owner: {self.owner} in Post: {self.created_time}"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=255)
