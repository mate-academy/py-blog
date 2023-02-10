from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"post '{self.title}' by {self.owner}"


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    def __str__(self):
        return f"comment to " \
               f"{self.post} by " \
               f"{self.user} from " \
               f"{self.created_time}"
