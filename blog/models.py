from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("blog:user-detail", kwargs={"pk": self.pk})


class Post(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="comments")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
