from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return f"{self.username}: {self.get_full_name()}"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-created_time"]

    @property
    def number_of_comments(self):
        return self.commentaries.count()

    def __str__(self) -> str:
        return f"{self.title} ({self.owner})"


class Commentary(models.Model):
    user = models.ForeignKey(
        User, related_name="commentaries", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="commentaries", on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"
        ordering = ["-created_time"]

    @property
    def short_content(self):
        short = self.content[:50]

        if len(self.content) > 50 and not self.content.endswith("..."):
            return short + "..."

        return short
