from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="posts")

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.commentary.count()


class Commentary(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="commentary")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="commentary")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
