from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}, {self.first_name}, {self.last_name}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="posts"
    )

    def __str__(self):
        return f"{self.owner}, {self.title}, {self.content}"


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.user}, {self.post}, {self.content}"
