from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Commentary, Post, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_time",
        "owner",
    ]
    list_filter = [
        "owner",
    ]
    search_fields = [
        "title",
        "owner",
    ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "post",
        "user",
        "created_time",
    ]
    list_filter = [
        "user",
    ]
    search_fields = [
        "post",
        "user",
    ]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
