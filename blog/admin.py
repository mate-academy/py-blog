from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Post, User, Commentary
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name")
    search_fields = ("username",)
    list_filter = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_time")
    search_fields = ("title",)
    list_filter = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_time")
    search_fields = ("user",)
    list_filter = ("user",)


admin.site.unregister(Group)
