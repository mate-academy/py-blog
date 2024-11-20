from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("blog:user-detail", kwargs={"pk": self.pk})


class Post(models.Model):
    owner = (
        models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING
        )
    )
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    created_time = models.DateTimeField(max_length=255)

    class Meta:
        ordering = ["created_time"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.DO_NOTHING
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["created_time"]
