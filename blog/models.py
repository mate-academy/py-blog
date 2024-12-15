from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.content
