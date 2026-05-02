from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        created_at = self.created_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.title} by {self.owner}, created at {created_at}"

    class Meta:
        ordering = ["-created_time"]


class User(AbstractUser):
    pass

    class Meta:
        verbose_name_plural = "users"
        ordering = ["username"]


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="comments")

    def __str__(self):
        created_at = self.created_time.strftime("%Y-%m-%d %H:%M:%S")
        content_preview = self.content[:30]
        return (f"by {self.user} "
                f"comments: {content_preview}...  at {created_at}")
