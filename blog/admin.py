from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "last_name"]
    list_filter = ["username"]
    search_fields = ["username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_time"]
    list_filter = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "created_time"]
    list_filter = ["created_time"]


admin.site.unregister(Group)
