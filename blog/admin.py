from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_time", "owner"]
    list_filter = ["owner"]
    search_fields = ["title"]
    search_help_text = "enter a title to search"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["post", "created_time", "user"]
    list_filter = ["post", "user"]
    search_fields = ["content"]


admin.site.unregister(Group)
