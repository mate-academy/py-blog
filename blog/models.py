from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from blog_system import settings


class User(AbstractUser):
    class Meta:
        ordering = ("username",)

    def get_absolute_url(self):
        return reverse("blog:user-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Post: "
            f"{self.title}. "
            f"Owner: {self.owner} (created at {self.created_time}"
        )

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    def __str__(self):
        return (
            f"Commentary for {self.post} post "
            f"from {self.user} (created: {self.created_time}"
        )
