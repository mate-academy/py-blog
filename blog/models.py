from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = models.ForeignKey(User, null=True,
                             on_delete=models.SET_NULL,
                             related_name="comments")
    post = models.ForeignKey(Post, null=True,
                             on_delete=models.SET_NULL,
                             related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
