from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary

# 1. Вимикаємо Group у адмінці
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_superuser")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time",)
    search_fields = ("title", "content")
    date_hierarchy = "created_time"
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("content", "user__username")
    list_filter = ("created_time",)
