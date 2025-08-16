from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("id", "owner", "title", "created_time")
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("created_time",)
    list_display = ("id", "user", "content", "post", "content", "created_time")
    search_fields = ("content",)


admin.site.unregister(Group)
