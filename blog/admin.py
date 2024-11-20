from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class AdminUser(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                )
            },
        ),
    )


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["title", "content", "created_time", "owner"]
    search_fields = ["title"]
    list_filter = ["owner"]


@admin.register(Commentary)
class AdminCommentary(admin.ModelAdmin):
    list_display = ["user", "content", "post", "created_time"]
    search_fields = ["content"]
    list_filter = ["user"]


admin.site.unregister(Group)
