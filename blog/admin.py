from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = (
        "title",
        "content",
    )
    list_filter = (
        "created_time",
        "owner",
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):

    search_fields = ("content",)
    list_filter = (
        "created_time",
        "user",
        "post",
    )
