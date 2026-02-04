from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_superuser")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("created_time", "owner")
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "content", "created_time")
    search_fields = ("content", "user__username", "post__title")
    list_filter = ("created_time", "user", "post")
    ordering = ("-created_time",)
