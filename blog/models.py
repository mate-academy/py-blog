from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}: {self.content}"


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentary"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return (
            f"User: {self.user.username}, Post title: {self.post.title}, "
            f"Create_time: {self.created_time}/n"
            f"Content: {self.content}"
        )
