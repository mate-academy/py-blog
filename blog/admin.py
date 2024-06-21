from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "created_time",
    )
    list_filter = ("owner",)
    search_fields = (
        "owner__username",
    )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
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


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_time",
        "post",
    )
    list_filter = (
        "user",
        "post",
    )
    search_fields = (
        "user__username",
        "post__title",
    )


admin.site.unregister(Group)
