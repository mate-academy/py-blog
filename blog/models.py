from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group
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
    created_time = models.DateTimeField(default=timezone.now)

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
    created_time = models.DateTimeField(default=timezone.now)
    content = models.TextField()
