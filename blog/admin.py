from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


# Unregister the Group model
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    search_fields = ["username", "email"]
    list_display = ["username", "email", "first_name", "last_name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "owner__username"]
    list_display = ["title", "owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["content", "user__username"]
    list_display = ["user", "post", "created_time"]
