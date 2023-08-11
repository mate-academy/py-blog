from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from blog_system import settings


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ["-created_time"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])

    def __str__(self):
        return f"Post {self.id}: {self.owner} - {self.title}"


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "commentaries"

    def __str__(self):
        return f"Commentary ({self.id} to post {self.post})"
