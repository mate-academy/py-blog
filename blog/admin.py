from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email")
    ordering = ("id",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("owner", "title", "created_at")
    list_filter = ("owner", "created_time")
    ordering = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user", "created_at")
    list_filter = ("user", "created_time")
    ordering = ("created_time",)


admin.site.unregister(Group)
