from django.contrib.auth.models import AbstractUser
from django.db import models
from wheel.metadata import _


class User(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
        verbose_name=_("Groups"),
        help_text=_(
            "The groups this user belongs to. "
            "A user will get all permissions "
            "granted to each of their groups."
        ),
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True,
        verbose_name=_("User permissions"),
        help_text=_("Specific permissions for this user."),
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return f"Owner: {self.owner}, post: {self.title}"


class Commentary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]
