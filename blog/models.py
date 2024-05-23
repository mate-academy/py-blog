from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Count
from django.urls import reverse

from blog_system import settings


class User(AbstractUser):
    email = models.CharField(max_length=63)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created_time"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
