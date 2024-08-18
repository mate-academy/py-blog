from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ...


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} by {self.owner}"


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1024)
