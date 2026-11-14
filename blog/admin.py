from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name",
                    "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time", "content")
    list_filter = ("owner", "title", "created_time")
    search_fields = ("content", "title")


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    search_fields = ("content",)

admin.site.unregister(Group)
