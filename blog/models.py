from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):

    first_name = models.CharField(
        max_length=255)
    last_name = models.CharField(
        max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_time"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[self.pk])


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="comments")

    def __str__(self) -> str:
        return f"{self.user} ({self.created_time})"

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"
        ordering = ["-created_time"]
