from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "owner",
        "created_time",
    ]
    list_filter = [
        "owner",
        "title",
        "created_time",
    ]
    search_fields = [
        "owner",
        "title",
        "created_time",
    ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "post",
        "created_time",
        "content",
    ]
    list_filter = [
        "user",
        "created_time",
    ]
    search_fields = [
        "user",
        "created_time",
    ]


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "username",
                )
            }
        ),
    )
