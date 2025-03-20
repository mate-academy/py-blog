from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f'{self.owner.first_name} {self.owner.last_name} "{self.title}"'


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "commentaries"
        ordering = ["-created_time"]

    def __str__(self):
        return (
            f'{self.user.first_name} {self.user.last_name}: "{self.content}"'
        )
