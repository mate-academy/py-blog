from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField()

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentaries", default=1
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries", default=1
    )
    content = models.TextField()
    created_time = models.DateTimeField()

    def __str__(self):
        return f"Commentary #{self.id}"

    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "custom-textarea"}),
    )

    class Meta:
        model = Commentary
        fields = ["content"]
