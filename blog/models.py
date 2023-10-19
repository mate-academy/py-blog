from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def __str__(self) -> str:
        return f"{self.username} ({self.get_full_name()})"


class Post(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} #{self.id}"

    def get_absolute_url(self) -> str:
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.pk},
        )


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="commentaries",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        to="blog.Post", related_name="commentaries", on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return f"Commentary #{self.id}"
