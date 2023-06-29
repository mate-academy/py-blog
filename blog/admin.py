from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Commentary
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "email",
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("post",)
    list_filter = ("created_time",)
