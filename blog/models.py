from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )


class User(AbstractUser):
    pass


class Commentary(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
