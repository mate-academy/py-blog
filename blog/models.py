from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=63)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=63)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=63)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "commentaries"
        ordering = ["created_time"]
