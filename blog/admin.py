from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    list_filter = ("created_time",)


admin.site.unregister(Group)
