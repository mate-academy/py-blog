from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "owner__username")
    list_filter = ("created_time", "owner",)
    list_display = ("title", "owner", "created_time",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", "email",)
    list_filter = ("username",)
    list_display = UserAdmin.list_display + ("username",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user__username", "post__title",)
    list_filter = ("created_time", "user",)
    list_display = ("post", "user", "created_time",)
