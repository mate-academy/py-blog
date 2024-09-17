from django.contrib import admin
from django.contrib.auth.admin import Group, UserAdmin

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time", ]
    list_filter = ["owner", "title", "created_time", ]
    search_fields = ["title", "owner", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time", ]
    list_filter = ["user", "post", "created_time", ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")


admin.site.unregister(Group)
