from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("username", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "owner__username", "content")
    list_filter = ("owner", "created_time")
    list_display = ("title", "owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("post__title", "user__username", "content")
    list_filter = ("post__title", "user__username", "created_time")
    list_display = ("post", "user", "created_time")


admin.site.unregister(Group)
