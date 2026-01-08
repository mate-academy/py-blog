from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Post(models.Model):
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at:"
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at:"
    )
    content = models.TextField(verbose_name="Add commentary: ")

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "commentary"
        verbose_name_plural = "comments"
