from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    # Fields from AbstractUser already contain username,
    # email, first_name, last_name, password
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

    @property
    def comments_count(self):
        return self.comments.count()


class Commentary(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"
