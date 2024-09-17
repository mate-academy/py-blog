from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner")
    search_fields = ("title",)
    list_filter = ("owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "created_time")
    list_filter = ("post", "user")


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display


admin.site.unregister(Group)
