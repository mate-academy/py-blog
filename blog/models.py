from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from blog_system import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self):
        return f"{self.title} {self.content} {self.created_time}"

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="commentaries"
    )

    def __str__(self):
        return f"{self.content}, created_ad: {self.created_time}"


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
