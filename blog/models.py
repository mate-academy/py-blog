from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_time",)

class Commentary(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="commentary_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentary")
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.post}"

    class Meta:
        ordering = ("-created_time",)
