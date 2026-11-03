from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "content",
        "created_time",
    )
    list_filter = ("owner",)
    search_fields = ("title",)


class UserModelAdmin(UserAdmin):
    pass


@admin.register(Commentary)
class CommentaryModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
        "content",
        "created_time",
    )
    list_filter = ("user",)


admin.site.unregister(Group)
