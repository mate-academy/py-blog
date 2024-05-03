from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    created_time = models.TextField()


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name="commentary",
        on_delete=models.CASCADE
    )
    created_time = models.TextField()
    content = models.TextField()
