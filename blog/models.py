from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ['username']


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_time']
        verbose_name = ['posts']

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_time']
        verbose_name = ['comments']

    def __str__(self) -> str:
        if len(self.content) >= 15:
            return f"{self.content[:15]}..."
        return self.content
