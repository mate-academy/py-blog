from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(null=False)


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    content = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
