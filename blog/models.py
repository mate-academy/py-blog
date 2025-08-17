from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.owner.username}"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.post.title} - {self.user.username}"
