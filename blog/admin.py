from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name"]
    list_filter = ["username"]
    search_fields = ["username", "first_name", "last_name"]


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["owner", "created_time"]
    search_fields = ["title", "owner", "created_time"]


@admin.register(Commentary)
class AdminCommentary(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user", "created_time"]
    search_fields = ["user", "post", "created_time"]


admin.site.unregister(Group)
