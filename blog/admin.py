from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "email")}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    search_fields = ("owner__username", "title")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user__username",)
    list_display = (
        "post",
        "short_content",
        "user",
        "created_time",
    )
    list_filter = ("created_time",)

    def short_content(self, obj):
        max_length = 50
        return (
            (obj.content[:max_length] + "...")
            if len(obj.content) > max_length
            else obj.content
        )

    short_content.short_description = "Content"


admin.site.unregister(Group)
