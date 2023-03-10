from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_time")
    list_filter = ["created_time"]
    search_fields = ["owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("content", "created_time")
    filter_fields = ["created_time"]
    search_fields = ["owner"]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
