from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Post(models.Model):

    class Meta:
        ordering = ["-created_time"]

    owner = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, default="Author unknown"
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):

    class Meta:
        ordering = ["created_time"]

    user = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, default="Author unknown"
    )
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s comment"
