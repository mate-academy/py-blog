from django.contrib import admin
from .models import Post, User, Commentary
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "created_time")
    search_fields = ("title", "content", "owner__username")
    list_filter = ("created_time", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_time")
    search_fields = ("content", "user__username", "post__title")
    list_filter = ("created_time",)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


admin.site.unregister(Group)
