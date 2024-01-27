from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    search_fields = ["post"]
    list_filter = ["user"]


admin.site.unregister(Group)
