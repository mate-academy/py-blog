from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_filter = BaseUserAdmin.list_filter + ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("owner",)
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("post",)
    search_fields = ("user__username", "content")


admin.site.unregister(Group)
