from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Commentary, Post

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets
    search_fields = ("username", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time")
    search_fields = ("owner", "title", "content", "created_time")
    list_filter = ("created_time", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    search_fields = ("user", "post", "created_time", "content")
    list_filter = ("created_time",)
