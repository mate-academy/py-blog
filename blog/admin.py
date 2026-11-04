from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined"
    ]
    list_filter = ["username", "first_name", "last_name"]
    search_fields = ["username", "first_name", "last_name"]
    ordering = ["-date_joined"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    list_filter = ["created_time"]
    search_fields = ["title", "content"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    list_filter = ["created_time"]


admin.site.unregister(Group)
