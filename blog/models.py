from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    username = models.EmailField(max_length=255, unique=True)

    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name="groups",
    #     blank=True,
    #     help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    #     related_name="blog_users",
    #     related_query_name="blog_user"
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name="user permissions",
    #     blank=True,
    #     help_text="Specific permissions for this user.",
    #     related_name="blog_users",
    #     related_query_name="blog_user"
    # )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("blog:user-detail", kwargs={"pk": self.pk})


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentaries")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentaries")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.content
