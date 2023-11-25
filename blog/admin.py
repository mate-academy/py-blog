from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["created_time", "owner", "title", "content"]
    list_filter = ["owner", "created_time", "title"]
    search_fields = ["id", "owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["created_time", "user", "post"]
    list_filter = ["created_time", "user", "post"]
    search_fields = ["created_time", "user", "post"]


@admin.register(User)
class UserAuthorAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
