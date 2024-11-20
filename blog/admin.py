from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "title", "created_time")
    list_filter = ("owner",)
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_time")
    list_filter = ("user", "post")
    search_fields = ("content",)
