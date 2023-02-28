from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "title",
        "content",
        "created_time"
    ]
    list_filter = [
        "created_time",
        "owner",
        "title"
    ]
    search_fields = [
        "owner__username"
    ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "post",
        "created_time",
        "content"
    ]
    list_filter = [
        "user",
        "created_time"
    ]
    search_fields = [
        "user__username"
    ]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
