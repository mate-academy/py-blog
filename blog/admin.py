from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Commentary, Post

admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name", "username", "email"]

admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_filter = ["created_time", "owner", "content", "title"]
    list_display = ["title", "content"]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)


class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["post", "created_time", "user", "content"]

admin.site.register(Commentary, CommentaryAdmin)