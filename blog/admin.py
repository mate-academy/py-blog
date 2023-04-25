from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["created_time", "title", "owner"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["created_time", "post", "user"]
    list_filter = ["user", "post"]
    search_fields = ["content"]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
