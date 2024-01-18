from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User,
                              related_name="posts",
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_time",)

    def __str__(self):
        return (f"Post: {self.title}, "
                f" posted by: {self.owner} at {self.created_time}")


class Commentary(models.Model):
    user = models.ForeignKey(User,
                             related_name="comments",
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name="comments",
                             on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ("created_time",)

    def __str__(self):
        return f"Comment {self.content} by {self.user.username}"
