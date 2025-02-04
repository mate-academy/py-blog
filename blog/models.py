from django.contrib.auth.models import AbstractUser
from django.db import models

from blog_system import settings


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.owner}: {self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"

    def __str__(self) -> str:
        return f"{self.user.username}: {self.post}"
