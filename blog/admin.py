from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ("user", "post")
    search_fields = ("user__username", "post__title", "content")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "text", "created_time")
    list_filter = ("title", "owner")
    search_fields = ("owner", "title", "content")

    @staticmethod
    def text(obj):
        return (
            obj.content[:50] + "..."
            if len(obj.content) > 50
            else obj.content
        )
