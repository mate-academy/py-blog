from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    search_fields = ["username"]
    list_filter = ["first_name", "last_name", "username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["owner__username", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_filter = ["user__username", "created_time"]


admin.site.unregister(Group)
