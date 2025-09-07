from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_time"]
    list_filter = [
        "created_time",
    ]
    search_fields = ["title", "content"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "created_time"]
    list_filter = [
        "created_time",
    ]


admin.site.unregister(Group)
