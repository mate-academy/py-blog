from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.fieldsets


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "content",
        "created_time",
    )
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "user",
        "content",
        "created_time",
    )
