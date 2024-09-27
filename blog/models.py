from django.db import models
from django.contrib.auth.models import AbstractUser
from blog_system.settings import AUTH_USER_MODEL


class Commentary(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "Post",
        related_name="comments",
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
