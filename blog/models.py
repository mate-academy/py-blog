from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return (f"{self.username} {self.first_name}"
                f" {self.last_name} {self.email}")

    class Meta:
        ordering = ("username",)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="posts",
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} / {self.created_time}"

    class Meta:
        ordering = ("title",)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="commentaries",
                               on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name="commentaries",
                             on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.author} / {self.created_date}"

    class Meta:
        verbose_name_plural = "Comments"
