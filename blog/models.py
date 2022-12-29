from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        ordering = ["username"]


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2500)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return self.title

    def num_of_comments(self):
        num_of_comments = Commentary.objects.filter(post_id=self.id).count()
        return num_of_comments


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)

    class Meta:
        ordering = ["created_time"]
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"

