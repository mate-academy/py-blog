from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UseAdmin(UserAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post")
