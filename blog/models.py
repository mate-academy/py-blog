from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-created_time",
        ]

    def __str__(self):
        return f"{self.title} ({self.created_time})"


class Commentary(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return {self.content}


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("username",)
