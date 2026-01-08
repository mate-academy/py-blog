from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
