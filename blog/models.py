from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})

    def __str__(self):
        display_content = self.content
        if len(display_content) > 25:
            display_content = display_content[:25] + "..."

        return f"{self.owner.username} - {self.title}: {display_content}"


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries",
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        display_title = self.post.title
        display_comment = self.content

        if len(display_title) > 25:
            display_title = display_title[:25] + "..."
        if len(display_comment) > 25:
            display_comment = display_comment[:25] + "..."

        return f"{self.user.username}: {display_title} - {display_comment}"
