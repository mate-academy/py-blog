from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def get_absolute_url(self):
        return "/"


class Post(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
