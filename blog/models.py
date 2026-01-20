from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    password = models.CharField(max_length=128)


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_user"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)


class Commentary(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="comm_user"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comm_post"
    )
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
