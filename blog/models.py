from django.contrib.auth.models import AbstractUser
from django.db import models
from blog_system.settings import AUTH_USER_MODEL


class User(AbstractUser):
    pass


class Post(models.Model):
    objects = models.Manager()
    owner = models.ForeignKey(AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="comments")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
