from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post"
    )
    title = models.CharField(max_length=65)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comment"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        related_name="commentary"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
