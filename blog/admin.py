from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_filter = ["first_name", "last_name"]
    search_fields = ["username", "first_name", "last_name"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        "content",
        "created_time",
    )
    list_filter = ["created_time"]
    search_fields = ["content"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        "created_time",
        "owner"
    )
    list_filter = ["title", "created_time", "owner"]
