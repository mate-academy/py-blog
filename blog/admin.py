from blog.models import User, Post, Commentary
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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
        "first_name",
        "last_name",
        "email",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "title",
        "content",
    )
    search_fields = (
        "owner",
        "title",
    )
    list_filter = (
        "owner",
        "title",
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
    )
    search_fields = (
        "user",
        "post",
    )
    list_filter = (
        "user",
        "post",
    )
