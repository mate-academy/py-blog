from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField(
        max_length=255)
    last_name = models.CharField(
        max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return f"{self.user.username}'s comment on {self.post.title}"
