from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "title",
        "content",
        "created_time",
    ]
    search_fields = (
        "owner__username",
        "title",
        "content",
        "created_time",
    )
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "post",
        "content",
        "created_time",
    ]
    search_fields = (
        "user__username",
        "post__title",
        "content",
        "created_time",
    )
    list_filter = ("created_time",)
