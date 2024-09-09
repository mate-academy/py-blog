from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["owner", "title", "content", "created_time", ]
    search_fields = ["owner", "title", "content"]
    list_filter = ["owner", "created_time", ]


@admin.register(Commentary)
class CommentAdmin(ModelAdmin):
    list_display = ["post", "user", "content", "created_time", ]
    search_fields = ["user", "title", ]
    list_filter = ["user", "post", "created_time", ]


admin.site.unregister(Group)
