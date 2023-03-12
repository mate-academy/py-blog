from django.contrib.auth.models import AbstractUser
from django.db import models
from blog_system import settings
from django.template.defaultfilters import truncatechars


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    # def __str__(self):
    #     return truncatechars(self.content, 25)
    def __str__(self):
        return self.content
