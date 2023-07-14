from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.CharField(max_length=255)


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"
