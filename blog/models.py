from django.contrib.auth.models import AbstractUser
from django.db import models
from django.http import HttpResponse
from django.urls import reverse

from blog_system import settings


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ["-created_time"]

    def get_absolute_url(self) -> HttpResponse:
        return reverse("blog:post-detail", kwargs={"pk": str(self.pk)})


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
