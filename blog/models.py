from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        ordering = ["username"]


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="users", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="commentaries", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "commentaries"
