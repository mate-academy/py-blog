from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Comments"
