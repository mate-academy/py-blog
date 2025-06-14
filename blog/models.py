from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username}) "


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="Enter your text")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Time creat")

    def __str__(self):
        return f"{self.title} | Posted: {self.created_time}"


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default=None, help_text="Enter your text")

    def __str__(self):
        return f"{self.user} name of post:{self.post}"
