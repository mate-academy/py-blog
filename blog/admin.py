from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "password"]
    search_fields = ["username", "first_name", "last_name", "email"]
    list_filter = ["is_staff", "is_superuser", "username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    search_fields = ["title", "owner__username"]
    list_filter = ["created_time", "title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", "content"]
    search_fields = ["user__username", "post__title"]
    list_filter = ["created_time"]
