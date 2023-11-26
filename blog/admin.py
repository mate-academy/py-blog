from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Commentary, Post
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    search_fields = (
        "username",
        "email",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "title",
        "content",
        "created_time",
    )
    list_filter = ("owner", "created_time")
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
        "content",
        "created_time",
    )
    list_filter = (
        "user",
        "post",
    )
