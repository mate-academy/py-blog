from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Commentary(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.post} {self.content}"


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username
