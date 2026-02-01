from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from blog_system import settings


class User(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Post(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self):
        return f"{self.created_time}: {self.title} ({self.owner})"

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment to post {self.post.title} by {self.user}"
