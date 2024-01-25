from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    password = models.CharField(max_length=255)

    class Meta:
        pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=4096)
    created_time = models.CharField(max_length=64)

    class Meta:
        pass


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.CharField(max_length=64)
    content = models.CharField(max_length=4096)

    class Meta:
        pass
