from django.contrib import admin

from blog.models import User, Post, Commentary
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(Group)


@admin.register(User)
class DriverAdmin(UserAdmin):
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("username", "email", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")
    search_fields = ("owner", "title", "content", "created_time")
    list_filter = ("owner", "title", "content", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("user__username", "post__title", "post__owner__username", "created_time")
    list_filter = ("user", "post__title", "created_time")
