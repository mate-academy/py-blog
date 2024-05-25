from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="posts"
    )


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="user_comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="post_comments"
    )

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
