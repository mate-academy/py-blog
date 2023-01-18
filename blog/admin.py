from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Commentary, User, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "owner",
        "created_time",
    ]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    list_filter = ["post__title"]
