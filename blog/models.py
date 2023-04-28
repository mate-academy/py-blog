from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    @staticmethod
    def get_absolute_url():
        return reverse("blog:index")


class Post(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.title} (by {self.owner} at {self.created_time})"

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="commentaries")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["post", "-created_time"]
        verbose_name_plural = "commentaries"

    def __str__(self):
        return (f"Commentary #{self.id} "
                f"(by {self.user} under {self.post.title})")

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.post.pk})
