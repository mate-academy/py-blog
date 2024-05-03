from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system.settings import AUTH_USER_MODEL


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE
    )


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        AUTH_USER_MODEL, related_name="commentaries", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="commentaries", on_delete=models.CASCADE
    )
