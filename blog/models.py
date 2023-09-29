from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="commentaries",
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "commentaries"
        ordering = ("-created_time",)


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

    class Meta:
        ordering = ("-created_time",)

    def num_comments(self) -> int:
        return self.commentaries.all().count()
