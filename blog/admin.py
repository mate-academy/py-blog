from django.contrib import admin

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]
    list_filter = ["first_name", "last_name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "title",
        "created_time",
    ]
    list_filter = ["created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "post",
        "created_time",
    ]
    list_filter = ["created_time"]
