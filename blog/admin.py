from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    add_fieldsets = UserAdmin.add_fieldsets + (
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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "owner",
        "created_time",
    ]
    list_filter = [
        "created_time",
    ]
    search_fields = ["title", "created_time"]


admin.site.register(Commentary)
admin.site.unregister(Group)
