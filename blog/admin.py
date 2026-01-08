from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from blog.models import (
    Commentary,
    Post,
    User
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            (
                "User info",
                {
                    "fields": (
                        "username",
                        "email",
                        "password1",
                        "password2",
                    )
                }
            ),
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
    list_display = ("owner", "title", "created_time",)
    list_filter = ("created_time", "owner",)
    search_fields = ("content", "title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post_title", "created_time",)
    list_filter = ("created_time", "user",)
    search_fields = ("content", "post__title",)

    def post_title(self, obj):
        return (
            obj.post.title[:12] + "..."
            if len(obj.post.title) > 15
            else obj.post.title[:15]
        )

    post_title.short_description = "title"


admin.site.unregister(Group)
