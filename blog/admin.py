from django.contrib import admin
from .models import User, Post, Commentary
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")
    search_fields = ["username"]


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time",)
    search_fields = ["title", "content"]


@admin.register(Commentary)
class CommentaryModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "content",
    )
    list_filter = ("created_time",)
    search_fields = ["content", "user__username"]
