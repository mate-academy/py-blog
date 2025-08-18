from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey


class Post(models.Model):
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.content


class User(AbstractUser):
    pass

    def __str__(self):
        return f"({self.username}) {self.first_name} {self.last_name}"
