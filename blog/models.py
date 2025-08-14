from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}: ({self.first_name}, {self.last_name})"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        related_name="user_comments",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="post_comments",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"
        ordering = ["created_time"]

    def __str__(self):
        return f"{self.user}: {self.content[:30]}\n{self.created_time}"
