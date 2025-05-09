from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        "Post",
         on_delete=models.CASCADE,
         related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class User(AbstractUser):

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username