from django.db import models
from django.contrib.auth.models import AbstractUser


from blog_system.settings import AUTH_USER_MODEL


class Post(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return f"{self.title} (by {self.owner})"


class User(AbstractUser):
    pass


class Commentary(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self) -> str:
        return f"Commentary for {self.post}"
