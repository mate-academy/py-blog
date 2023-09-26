from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name", ]
    list_filter = ["username", ]
    search_fields = ["username", "email", ]


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["owner", "title", "content", "created_time", ]
    list_filter = ["owner", "title", "created_time", ]
    search_fields = ["owner", "title", ]


@admin.register(Commentary)
class CommentaryAdmin(ModelAdmin):
    list_display = ["user", "post", "created_time", "content", ]
    list_filter = ["user", "post", "created_time", ]
    search_fields = ["user", "post", ]
