from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=20)


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=33)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def comment_count(self):
        return self.commentary.count()


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
