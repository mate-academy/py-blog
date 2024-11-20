from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class PersonAdmin(UserAdmin):
    search_fields = [
        "username",
    ]
    list_filter = [
        "first_name",
        "last_name",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "owner__username", "content"]
    list_filter = ["created_time", "owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = [
        "post",
        "user__username",
    ]
    list_filter = ["created_time", "user"]


admin.site.unregister(Group)
