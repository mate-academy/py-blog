from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["user", "created_time"]
    list_display = ["user", "post", "created_time"]
    search_fields = ["content"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["created_time", "owner"]
    list_display = ["id", "owner", "title", "created_time"]
    search_fields = ["content"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["username"]
