from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(max_length=63, blank=False)
    last_name = models.CharField(max_length=63, blank=False)

    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ("-created_time",)

    def __str__(self) -> str:
        return f"{self.title} by {self.owner}"

    def get_absolute_url(self) -> str:
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Commentaries"
        ordering = ("-created_time",)

    def __str__(self) -> str:
        return f"Comment on {self.post.title} by {self.user}"
