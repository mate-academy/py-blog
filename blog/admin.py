from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_time", "owner_id"]
    list_filter = ["created_time"]
    search_fields = ["title", "owner_id", "content"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["id", "created_time", "user_id", "post_id", "content"]
    list_filter = ["created_time"]
    search_fields = ["user_id", "post_id", "content"]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
