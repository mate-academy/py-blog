from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    search_fields = ["username", "email"]
    list_filter = ["username", "first_name", "last_name", "email"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    search_fields = ["owner__username", "title", "content"]
    list_filter = ["created_time", "title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):

    search_fields = ["user__username", "post__title", "content"]
    list_filter = ["created_time", "post__title"]


admin.site.unregister(Group)
