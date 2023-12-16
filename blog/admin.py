from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
    )
    search_fields = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("owner__username", "title")
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user__username", "content")
    list_filter = ("created_time",)
