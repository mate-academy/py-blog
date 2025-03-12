from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from blog_system import settings


# Create your models here.


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=(str(self.pk),))


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
