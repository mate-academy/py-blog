from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="posts"
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        verbose_name_plural = "Commentaries"
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.content
