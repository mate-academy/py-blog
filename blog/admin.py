from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["title", ]
    search_fields = ["title", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["post", ]
    search_fields = ["post", ]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
