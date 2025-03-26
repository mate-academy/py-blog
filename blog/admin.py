from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Post, Commentary, User
from django.contrib.auth.models import Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "content", "created_time")
    list_filter = ("owner",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_time")
    list_filter = ("user",)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ("username",)


admin.site.unregister(Group)
