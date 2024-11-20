from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content"]
    list_filter = ["created_time"]
    search_fields = ["owner", "title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content"]
    list_filter = ["post"]
    search_fields = ["user", "post"]


admin.site.unregister(Group)
