from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time", "content")
    list_filter = ["created_time", "title"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_time")
    list_filter = ["created_time"]
    search_fields = ["user", "post"]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
