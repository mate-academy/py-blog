from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username",)

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email",
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_time", ]
    search_fields = ("owner",)
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass
