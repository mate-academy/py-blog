from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from blog_system import settings


class User(AbstractUser):
    class Meta:
        ordering = ("username",)


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.CharField(max_length=255)


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="commentaries")
    created_time = models.DateTimeField(max_length=255,
                                        auto_now_add=True)
    content = models.TextField()
