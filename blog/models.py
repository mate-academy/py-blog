from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)