from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def comment_count(self):
        return self.commentary_set.count()


class Commentary(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content


class User(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.username
