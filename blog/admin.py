from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_staff",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("created_time", "owner")


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "user", "post", "created_time")
    search_fields = ("content",)
    list_filter = ("created_time", "user")
