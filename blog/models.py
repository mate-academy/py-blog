from django.contrib.auth.models import AbstractUser
from django.db import models
from blog_system import settings


# Create your models here


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=5000)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Commentaries"
        ordering = ["-created_time"]

    def __str__(self):
        return f"Created on {self.created_time.date()} "
