from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="commentaries",
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True, auto_created=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return f"{self.user} - {self.post}"
