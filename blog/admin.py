from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name"]
    search_fields = ["username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["created_time"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "created_time"]
    list_filter = ["created_time"]
    search_fields = ["post"]


admin.site.unregister(Group)
