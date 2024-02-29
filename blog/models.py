from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)

    def get_comments(self):
        return Commentary.objects.filter(post_id=self.id)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self):
        return (
            f"Comment by {self.user}:\n"
            f"{self.content[:20]}"
        )
