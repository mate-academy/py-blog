from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Post, User, Commentary

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    ordering = ("username",)


admin.site.register(Post)
admin.site.register(Commentary)
admin.site.unregister(Group)
