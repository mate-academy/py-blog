from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="posts",
        to="User"
    )
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(
        to="User", on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        to="Post", on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"


class User(AbstractUser):
    pass
