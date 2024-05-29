from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def num_comments(self):
        return self.commentaries.count()

    class Meta:
        ordering = ("-created_time", )


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="commentaries")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentaries")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ("-created_time", )
        verbose_name_plural = "Commentaries"
