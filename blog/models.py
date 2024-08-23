from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("owner", "created_time",)

    def __str__(self):
        return f"{self.owner}, '{self.title}'"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="commentary"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ("user", "created_time",)

    def __str__(self):
        return f"{self.user}, '{self.post.title}'"
