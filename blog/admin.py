from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_active")
    search_fields = ("username",)
    list_filter = ("is_superuser",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    ordering = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_time")
    search_fields = ("content",)
    list_filter = ("created_time",)
