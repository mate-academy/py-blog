from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="blog_user")
    user_permissions = models.ManyToManyField(
        Permission, related_name="blog_user"
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def short_content(self):
        if len(self.content) > 20:
            return self.content[:20] + "..."
        else:
            return self.content

    @property
    def short_title(self):
        char_length = 25
        if len(self.title) > char_length:
            return self.title[:char_length] + "..."
        else:
            return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        if len(self.content) > 20:
            return self.content[:20] + "..."
        else:
            return self.content
