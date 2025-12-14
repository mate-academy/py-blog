from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content", "owner__username")


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_time")
    list_filter = ("user", "post")
    search_fields = (
        "content",
        "user__username",
        "post__title",
    )
