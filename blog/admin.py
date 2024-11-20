from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("nickname", )
    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "nickname",
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
                    )
                },
            ),
        )
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user__username", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "owner__username", )


admin.site.unregister(Group)
