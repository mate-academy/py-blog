from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "post", ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "owner", ]
    search_fields = ["title", ]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display


admin.site.unregister(Group)
