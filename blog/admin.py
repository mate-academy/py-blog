from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User

admin.site.unregister(Group)


@admin.register(User)
class BlogAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    ]
    list_filter = ["is_active", "username", "is_staff"]
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional information",
         {"fields": ("first_name", "last_name", "email")}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "owner",
        "created_time",
    ]
    list_filter = [
        "created_time",
    ]
    search_fields = [
        "created_time",
    ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["post_id", "user", "created_time"]
    list_filter = ["created_time", "user"]
    search_fields = [
        "user",
    ]
