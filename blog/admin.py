from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time", ]
    list_filter = ["created_time", ]
    search_fields = ["title", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "created_time", ]
    list_filter = ["post", ]
    search_fields = ["post", "created_time", ]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", ]


admin.site.unregister(Group)
