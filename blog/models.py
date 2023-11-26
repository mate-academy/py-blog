from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(null=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        default_related_name = "commentaries"
        verbose_name_plural = "commentaries"
