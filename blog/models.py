from django.conf import settings  # noqa
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse  # noqa


# Create your models here.


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

    class Meta:
        ordering = ("username",)


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)

    def __str__(self) -> str:
        return f"{self.title[:15]}{'...' if len(self.title) > 15 else ''}"

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ("created_time",)
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return f"{self.content[:15]}{'...' if len(self.content) > 15 else ''}"

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])
