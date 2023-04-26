from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    ...

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    @staticmethod
    def get_absolute_url():
        return reverse(
            "blog:index",  # Will write user-detail
            # kwargs={"pk": self.pk}  # will use this
        )


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return (
            f"Owner: {self.owner.username}\n"
            f"(Title: {self.title}, created time: "
            f"{self.created_time.strftime('%d.%m.%Y (%H:%M)')})"
        )

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Commentary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentaries"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name="Comment")

    class Meta:
        ordering = ["post", "-created_time"]

        verbose_name = "commentary"
        verbose_name_plural = "commentaries"

    def __str__(self):
        return (
            f"Post: {self.post.title}\n"
            f"(Who: {self.user.username}, created time: "
            f"{self.created_time.strftime('%d/%m/%y (%H:%M)')})\n"
            f"({self.content})"
        )

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.post.pk})
