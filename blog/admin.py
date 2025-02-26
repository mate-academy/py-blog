from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ["username"]
    list_filter = ["username", "is_staff"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    search_fields = ["title"]
    list_filter = ["title", "owner__username"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "post", "user", "created_time"]
    search_fields = ["content"]
    list_filter = ["post__title", "user__username"]
