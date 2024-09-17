from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    created_time = models.DateTimeField(default=timezone.now)
    content = models.TextField()
