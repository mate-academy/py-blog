from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[self.pk])

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries",
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"
