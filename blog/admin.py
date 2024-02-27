from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("is_superuser",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "owner",
        "created_time",
    ]
    list_filter = ["created_time", "owner"]
    search_fields = [
        "title",
    ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "content",
        "created_time",
    ]
    list_filter = ["created_time", "user"]
    search_fields = [
        "content",
    ]


admin.site.unregister(Group)
