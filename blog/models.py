from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=20)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_unique_user_set',
        related_query_name='custom_unique_user',
    )


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="unique_post"
    )
    title = models.CharField(max_length=33)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="unique_commentary"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="unique_comment"
    )
    created_time = models.DateTimeField(default=timezone.now)
    content = models.TextField()
