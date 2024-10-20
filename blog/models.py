from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "users"
        ordering = ["username"]


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=63)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def commentary_count(self):
        return self.commentary.count()

    def __str__(self):
        return f"{self.title} by {self.owner} at {self.created_time}"


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
        return f"{self.content} by {self.user} at {self.created_time}"
