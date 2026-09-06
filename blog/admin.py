from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


@admin.register(User)
class BlogUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff",)
    search_fields = ("username", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_time")
    list_filter = ("created_time", "user")
    search_fields = ("content", "user__username")


admin.site.unregister(Group)
