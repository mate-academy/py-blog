from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-date_joined']


class Post(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "Posts"
        verbose_name = "Post"


class Commentary(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.content

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "Commentaries"
        verbose_name = "Commentary"
