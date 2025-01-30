from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ["username", "email"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["content"]


admin.site.unregister(Group)
