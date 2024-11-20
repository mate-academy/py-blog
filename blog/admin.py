from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time")
    search_fields = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_time",
        "post",
    )
    search_fields = ("post",)
    list_filter = ("user",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")
    search_fields = ("username", "last_name")
    list_filter = ("username", "last_name")


admin.site.unregister(Group)
