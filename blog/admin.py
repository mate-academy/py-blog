from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ["username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_time", "owner"]
    list_filter = ["owner", "created_time"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user", "created_time"]


admin.site.unregister(Group)
