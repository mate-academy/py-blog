from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", "first_name", "last_name", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "title", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content", "owner__username")
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "created_time")
    list_filter = ("created_time", "post", "user")
    search_fields = ("content", "post__title", "user__username")
    ordering = ("-created_time",)
