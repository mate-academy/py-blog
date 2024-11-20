from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name",)
    search_fields = ("username", "first_name", "last_name",)
    list_filter = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time",)
    search_fields = ("title", "content",)
    list_filter = ("created_time", "owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time",)
    search_fields = ("content",)
    list_filter = ("created_time", "user",)


admin.site.unregister(Group)
