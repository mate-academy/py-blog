from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Commentary, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username", "email")
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
    list_display = ("id", "owner", "title", "created_time")
    list_filter = ("owner",)
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_time")
    list_filter = ("user", "post")
    search_fields = ("content",)
    actions = ["delete_selected"]

    def delete_selected(self, request, queryset):
        queryset.delete()

    delete_selected.short_description = "Delete selected commentaries"


admin.site.unregister(Group)
