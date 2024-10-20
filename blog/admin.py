from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from django.contrib import admin
from blog.models import Post, User, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("is_staff", "is_active")
    search_fields = ("username", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("created_time", "owner")
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("created_time", "user")
    search_fields = ("content",)


admin.site.unregister(Group)
