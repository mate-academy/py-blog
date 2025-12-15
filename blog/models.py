from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL,
                      on_delete=models.CASCADE,
                      related_name="commentaries")
    post = ForeignKey(Post,
                      on_delete=models.CASCADE,
                      related_name="commentaries")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
