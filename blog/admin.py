from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("owner", "created_time")
    search_fields = (
        "title",
        "content",
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("user", "created_time")
    search_fields = (
        "post",
        "content",
    )
