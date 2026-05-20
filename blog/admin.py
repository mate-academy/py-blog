from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["created_time", "owner"]
    search_fields = ["title", "content"]
    ordering = ["-created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["created_time"]
    search_fields = ["content", "user__username", "post__title"]


admin.site.unregister(Group)
