from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    search_fields = ["title"]
    list_filter = ["created_time", "owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    search_fields = ["user", "content"]
    list_filter = ["created_time", "user"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
