from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[self.id])

    def get_comments_count(self):
        return self.comments.count()


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
        return f"Comment ({self.user.username})"
