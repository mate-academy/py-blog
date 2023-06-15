from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
    #
    # def get_absolute_url(self):
    #     return reverse("taxi:driver-detail", kwargs={"pk": self.pk})


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.owner}, '{self.title}'"


class Commentary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentaries")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentaries")
    created_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "commentaries"

    def __str__(self):
        return f"{self.user} comments {self.post}"
