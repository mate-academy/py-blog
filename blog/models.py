from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Commentary(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.post.title}'
    
class User(AbstractUser):
    pass
