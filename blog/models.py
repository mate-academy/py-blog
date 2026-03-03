from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class Post(models.Model):
    owner = models.ForeignKey(User, related_name="posts",
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(User, related_name="comments",
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
