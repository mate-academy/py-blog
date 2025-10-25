from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    list_filter = ("user", "post", "created_time")
    search_fields = ("content",)
    ordering = ("-created_time",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time", "content")
    list_filter = ("owner", "created_time")
    search_fields = ("title",)
    ordering = ("-created_time",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password")
    search_fields = ("username",)
    ordering = ("-username",)


admin.site.unregister(Group)
