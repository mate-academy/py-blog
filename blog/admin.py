from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username",)
    list_filter = ("date_joined",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("created_time",)
