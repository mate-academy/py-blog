from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from blog_system import settings


class User(AbstractUser):

    def __str__(self) -> str:
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse("blog:user-detail", kwargs={"pk": self.pk})


class Post(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self) -> str:
        return f"comment {self.id} for post {self.post.id}"
