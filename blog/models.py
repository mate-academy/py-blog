from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time", "pk"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[self.pk])


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries",
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["created_time", "pk"]
        verbose_name_plural = "commentaries"

    def __str__(self):
        return f"{self.user}: {self.content[:50]}"
