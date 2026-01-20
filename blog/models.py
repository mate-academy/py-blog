from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    class Meta:
        ordering = ("username", )


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    created_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owners"
    )

    class Meta:
        ordering = ("created_time", )

    def __str__(self):
        return (f"{self.title} (created: {self.created_time}, "
                f"owner: {self.owner.first_name} {self.owner.last_name})")

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.id)])


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=255)

    class Meta:
        ordering = ("created_time", )

    def __str__(self):
        return f"{self.user} (created: {self.created_time})"
