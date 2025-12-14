from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = ("title", "content")
    date_hierarchy = "created_time"
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time")
    list_filter = ("user", "created_time")
    search_fields = ("content",)
    date_hierarchy = "created_time"
    ordering = ("created_time",)
