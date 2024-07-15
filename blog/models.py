from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time"]


class User(AbstractUser):
    class Meta:
        ordering = ["username"]


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="posts")
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["created_time"]
        verbose_name_plural = "Commentaries"
