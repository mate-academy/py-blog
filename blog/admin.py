from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Comment


@admin.register(Comment)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_time", "content")
    list_filter = ("author", "post", "created_time")
    search_fields = ("content",)
    ordering = ("-created_time",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_time", "content")
    list_filter = ("author", "created_time")
    search_fields = ("title",)
    ordering = ("-created_time",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username",)
    ordering = ("-username",)


admin.site.unregister(Group)
