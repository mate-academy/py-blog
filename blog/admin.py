from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    ordering = ["-created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", "content"]
    ordering = ["created_time"]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    ordering = ["username"]


admin.site.unregister(Group)
