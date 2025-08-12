from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "created_time",
    )
    search_fields = (
        "title",
        "owner__username",
    )
    list_filter = (
        "title",
        "owner",
        "created_time",
    )
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
        "created_time",
    )
    search_fields = (
        "user__username",
        "post__title",
    )
    list_filter = (
        "user",
        "post",
        "created_time",
    )
    ordering = ("-created_time",)


admin.site.unregister(Group)
