from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin

from .models import Commentary, Post, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "owner",
        "created_time",
    )
    search_fields = ("title", "content")
    list_filter = ("owner", "created_time")


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "post",
        "created_time",
    )
    search_fields = ("post__title", "content",)
    list_filter = ("post", "user", "created_time")


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
