from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = [
        "owner",
        "created_time",
    ]
    search_fields = [
        "title",
        "content",
    ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = [
        "user",
        "post",
        "created_time",
    ]
    search_fields = [
        "content",
    ]
