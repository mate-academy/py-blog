from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Commentary, Post, User


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display
