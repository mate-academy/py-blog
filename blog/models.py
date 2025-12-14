from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def get_absolute_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.pk}
        )

    def __str__(self):
        return self.title


class Commentary(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return (
            f"Comment by {self.user.username} on {self.post.title}"
        )
