from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Commentary, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    search_fields = ["username", "first_name", "last_name", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", ]
    search_fields = ["user", ]
    list_filter = ["post", "user", ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time", ]
    search_fields = ["owner", "title", ]
    list_filter = ["owner", ]


admin.site.unregister(Group)
