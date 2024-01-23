from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "owner__username", "created_time")
    list_filter = ("created_time", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    search_fields = (
        "user__username",
        "post__title",
        "created_time",
        "content"
    )
    list_filter = ("created_time", "user", "post")


admin.site.unregister(Group)
