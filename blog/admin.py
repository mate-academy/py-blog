from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "owner")
    list_filter = ("owner", "created_time")
    list_display = (
        "title",
        "created_time",
        "owner",
    )


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("post", "created_time", "user")
    search_fields = ("post", "user")
    list_display = ("post", "created_time", "user")


admin.site.unregister(Group)
