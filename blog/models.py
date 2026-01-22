from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse


class User(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Post(models.Model):
    owner = ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    user = ForeignKey("User", on_delete=models.CASCADE,
                      related_name="comments")
    post = ForeignKey("Post", on_delete=models.CASCADE,
                      related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
