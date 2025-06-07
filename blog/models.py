from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-date_joined']
