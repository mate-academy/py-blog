from django.contrib.auth.admin import UserAdmin, Group

from blog.models import Post, Commentary, User
from django.contrib import admin

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = (
        "title",
        "created_time",
    )
    list_filter = (
        "title",
        "created_time",
    )
    list_display = ("title", "owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("created_time",)
    list_display = ("created_time", "user")


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
