from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = (
        "title",
        "owner__username",
        "owner__first_name",
        "owner__last_name",
        "owner__email"
    )
    ordering = ("title", "owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time")
    search_fields = (
        "post",
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email"
    )
    ordering = ("post", "user",)


admin.site.register(User, UserAdmin)
