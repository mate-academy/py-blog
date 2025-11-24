from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
