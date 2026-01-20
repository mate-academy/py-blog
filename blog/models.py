from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    created_time = models.CharField(max_length=255)

    class Meta:
        ordering = ("created_time",)

    def __str__(self):
        return str(self.title)


class Commentary(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    created_time = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.post.pk)])
