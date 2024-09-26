from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Commentary, Post
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    list_filter = ["created_time", "owner"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    list_filter = ["post", "created_time"]
    search_fields = ["post"]


admin.site.register(User, UserAdmin)
