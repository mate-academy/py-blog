from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.title}'


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentaries')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.created_time} {self.user.username}'
