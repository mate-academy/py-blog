from django.db import models
from django.contrib.auth.models import AbstractUser

from blog_system import settings


class User(AbstractUser):

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.username})"


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=299)
    created_time = models.CharField(max_length=255)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return f"{self.owner}: {self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentary")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentary")
    created_time = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ["post"]

    def __str__(self) -> str:
        return f"{self.user}: {self.content}"
