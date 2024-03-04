from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Commentary, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("nickname", "groups", )
    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "nickname",
                        "groups",
                    )
                },
            ),
        )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "nickname",
                        "groups",
                    )
                },
            ),
        )
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "owner", )
