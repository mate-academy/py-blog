from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username",)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("first_name", "last_name")},
        ),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_filter = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("user",)
