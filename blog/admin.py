from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Model

from blog.models import Post, Commentary, User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("id", "title", "owner", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = (
        "title",
        "content",
    )


@admin.register(Commentary)
class CommentaryAdmin(ModelAdmin):
    list_display = ("id", "post", "user", "created_time")
    list_filter = ("post", "user", "created_time")
    search_fields = (
        "content",
    )
