from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "content", "owner", "created_time"
    ]
    list_filter = ["owner", "created_time"]
    search_fields = ["title", "content"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "content", "user", "post", "created_time"
    ]
    list_filter = ["user", "created_time"]
    search_fields = ["content", ]


admin.site.unregister(Group)
