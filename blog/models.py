from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_time = models.DateTimeField()

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.content
