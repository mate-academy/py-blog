from blog_system import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"



class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time", ]


    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentaries")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentaries")
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time", ]

