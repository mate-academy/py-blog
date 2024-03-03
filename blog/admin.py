from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(User)
class OurAdmin(UserAdmin):
    ordering = ["username"]
    search_fields = ["username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "owner", "created_time"]
    ordering = ["created_time"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    ordering = ["user"]
    search_fields = ["user__username", "post__title"]


admin.site.unregister(Group)
