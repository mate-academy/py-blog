from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "user",
        "created_time",
    )
    list_filter = ("created_time",)
    search_fields = ("content",)
