from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Commentary, Post, User


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "created_time",
        "content",
    )
    list_filter = (
        "owner",
        "created_time",
    )
    search_fields = (
        "title",
        "content",
        "owner__username",
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
        "created_time",
        "content",
    )
    list_filter = (
        "user",
        "created_time",
    )
    search_fields = (
        "content",
        "user__username",
        "post__title",
    )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
