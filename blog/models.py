from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse


class User(AbstractUser):
    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> reverse:
        return reverse("blog:post-detail", args=[str(self.id)])

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "Commentaries"

    def __str__(self) -> str:
        commentary = get_object_or_404(Commentary.objects.select_related('user', 'post'), pk=self.id)
        return f"Commentary by {commentary.user.username} on {commentary.post.title}"
