from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Commentary
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time")
    search_fields = ("content",)
    list_filter = ("created_time",)

