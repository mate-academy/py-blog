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
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    search_fields = ("title", "content")
    list_filter = ("owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "post","user", "created_time"]
    list_filter = ("user",)
    search_fields = ("content", "user__username",)
