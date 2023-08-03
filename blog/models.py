from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2500)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="user_commentaries"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="post_commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self):
        return f"To post '{self.post.title}' from {self.user.username}"
