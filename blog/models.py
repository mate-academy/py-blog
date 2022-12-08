from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_time"]

    @property
    def num_comments(self):
        return len(self.commentaries.all())

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.title}"


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="commentaries", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created_time"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.content}"
