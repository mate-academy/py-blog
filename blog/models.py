
from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system.settings import AUTH_USER_MODEL


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time", )


class Commentary(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="commentaries")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"
