from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "is_staff"]
    search_fields = ["username", "first_name", "last_name"]
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
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


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", "content"]
    list_filter = ["post__title"]
    search_fields = ["post__title"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]


admin.site.unregister(Group)
