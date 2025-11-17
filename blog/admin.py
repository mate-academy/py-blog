from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    add_fieldsets = (
        UserAdmin.add_fieldsets
        + (
            (
                "Additional information",
                {"fields": ("first_name", "last_name", "email",)}
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner",)
    list_filter = ("title", "owner",)
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("created_time", "user", "post",)
    list_filter = ("user", "post",)


admin.site.unregister(Group)
