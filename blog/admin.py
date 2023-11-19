from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "owner", "title", "created_time", "content",
    )
    list_filter = ("owner", "created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user", "post", "content", "created_time"
    )
    select_related = ('post__title',)
    list_filter = ("user", "post", "created_time")
    ordering = ("created_time",)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
