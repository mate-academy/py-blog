from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    class Meta:
        ordering = ["username"]


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True)

    class Meta:
        ordering = ["-created_time"]
        indexes = [models.Index(fields=["created_time"])]

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse("blog:index")


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["created_time"]
        indexes = [models.Index(fields=["created_time"]), ]

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
