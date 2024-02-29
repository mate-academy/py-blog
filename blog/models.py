from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ("-created_time",)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )

    class Meta:
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return self.content


class User(AbstractUser):
    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'
