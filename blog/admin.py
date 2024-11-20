from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
        "date_joined"
    )
    search_fields = ("username", "email")
    list_filter = ("is_active", "is_staff", "is_superuser")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "created_time",
    )
    search_fields = (
        "title",
        "created_time",
    )
    list_filter = (
        "owner",
        "created_time",
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_time",
    )
    search_fields = ("user",)
    list_filter = ("created_time",)


admin.site.unregister(Group)
