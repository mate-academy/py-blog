from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True)
    created_time = models.DateTimeField(auto_now=True)


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_created=True, null=True)
    content = models.CharField(max_length=255, blank=True)
