from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=63)
    content = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def display_content(self):
        if len(self.content) > 100:
            return self.content[:100] + "..."
        return self.content

    def __str__(self):
        return f"{self.owner}: {self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)

    class Meta:
        ordering = ["post"]

    def __str__(self):
        return f"{self.user}: {self.content}"
