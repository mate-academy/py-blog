from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    search_fields = ["username", ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["owner", "created_time"]
    search_fields = ["title", "owner__username"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user", "created_time"]
    search_fields = ["content"]


admin.site.unregister(Group)
