from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("first_name", "last_name", "email")},
        ),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")
    list_filter = ("owner__username", "created_time")
    search_fields = ("owner__username", "title")
    ordering = ("title", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post__title", "created_time")
    list_filter = ("post__title", "created_time")
    search_fields = ("user__username", "post__title")
    ordering = ("post__title", "created_time")


admin.site.unregister(Group)
