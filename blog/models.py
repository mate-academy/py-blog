from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self):
        return self.title

    def commentaries_count(self):
        return self.commentaries.count()


class Commentary(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentary by {self.author} on {self.post}"
