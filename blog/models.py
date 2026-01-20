from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

app_name = "blog"


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]


class Commentary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[self.post.id])
