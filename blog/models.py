from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "comments"


class User(AbstractUser):
    pass
