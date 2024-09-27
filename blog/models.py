from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="your_user_related_name")
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="blog_user_permissions"
    )

    class Meta:
        ordering = ("username",)


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts")
    title = models.CharField(max_length=65)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)

    def __str__(self):
        return self


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commentaries")
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ("-created_time",)

    def __str__(self):
        return self
