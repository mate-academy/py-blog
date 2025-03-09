from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    title = models.CharField(max_length=255)  # Назва посту
    content = models.TextField()  # Текст посту
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="posts")

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comments.count()


class Commentary(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments")  # Пост, до якого належить коментар
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments")  # Автор коментаря
    content = models.TextField()  # Текст коментаря
    created_time = models.DateTimeField(auto_now_add=True)  # Час створення

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title}"
