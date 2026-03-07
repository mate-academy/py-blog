from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, 
                              on_delete=models.CASCADE, related_name="posts")


class Comment(models.Model):
    author = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE, related_name="comments")
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
