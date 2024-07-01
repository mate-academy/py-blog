from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} 'posted by {self.owner}'"


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="posts")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self):
        return f"{self.user}: {self.content}"
