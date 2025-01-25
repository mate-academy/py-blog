from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # model = User
    list_display = ("username", "email", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_time", "owner")
    list_filter = ("owner",)
    search_fields = (
        "title",
        "owner__username",
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "created_time",
        "content",
        "post",
        "user",
    )
    list_filter = (
        "post",
        "user",
    )
    search_fields = (
        "content",
        "post__title",
        "user__username",
    )
