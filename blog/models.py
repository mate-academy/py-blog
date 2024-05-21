from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    REQUIRED_FIELDS = ("email", "first_name", "last_name", "password")


class Post(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=66)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.title} by {self.owner} "
                f"at {self.created_time.strftime("%Y-%m-%d")}")


class Commentary(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=150)
