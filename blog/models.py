from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="author_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="author_permissions"
    )

    class Meta:
        ordering = ("username",)


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="authors"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Commentaries"
        ordering = ("created_time",)

    def __str__(self) -> str:
        return f"User: {self.user.username} Post: {self.post.title}."
