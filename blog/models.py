from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"

    def __str__(self):
        return self.content
