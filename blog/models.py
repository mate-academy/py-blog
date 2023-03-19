from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):

    class Meta:
        ordering = ["created_time"]

    owner = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, default="Author unknown"
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField()


class Commentary(models.Model):

    class Meta:
        ordering = ["created_time"]

    user = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, default="Author unknown"
    )
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField()
    content = models.TextField()

