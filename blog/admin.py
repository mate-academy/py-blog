from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "title",
        "content",
        "created_time",
    )
    search_fields = ("title",)
    list_filter = (
        "owner",
        "title",
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
        "content",
    )
    search_fields = ("user",)
    list_filter = (
        "user",
        "post",
    )


admin.site.unregister(Group)
