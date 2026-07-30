from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_filter = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    search_fields = [
        "username",
    ]


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_filter = [
        "owner",
    ]
    search_fields = [
        "title",
    ]


@admin.register(Commentary)
class CommentaryAdmin(ModelAdmin):
    list_filter = [
        "user",
        "post",
    ]
    search_fields = [
        "user__username",
    ]


admin.site.unregister(Group)
