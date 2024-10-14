from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["owner", "created_time"]
    list_display = ["title", "owner", "created_time"]
    ordering = ["-created_time", "owner__username"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["user", "created_time", "post"]
    list_display = ["user", "created_time", "post"]
    ordering = ["-created_time", "user__username"]


admin.site.unregister(Group)
