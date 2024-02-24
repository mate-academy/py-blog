from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name",)
    list_filter = ("username", "first_name", "last_name",)
    search_fields = ("username", "first_name", "last_name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time",)
    list_filter = ("owner", "title", "created_time",)
    search_fields = ("owner", "title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content",)
    list_filter = ("user", "post", "created_time",)
    search_fields = ("user", "post",)


admin.site.unregister(Group)
