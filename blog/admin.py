from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time", ]
    search_fields = ["title", ]
    list_filter = ["owner", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "created_time", ]
    search_fields = ["content", ]
    list_filter = ["user", ]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name", ]
    search_fields = ["username", ]
    list_filter = ["username", ]

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info about you:",
            {
                "fields":
                    (
                        "first_name",
                        "last_name",
                    )
            }
        ),
    )


admin.site.unregister(Group)
