from django.contrib import admin
from .models import Post, User, Commentary
from django.contrib.auth.models import Group

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Commentary)
admin.site.unregister(Group)


class PostAdmin(admin.ModelAdmin):
    search_fields = ("created_time", "owner", "title", "content")
    list_filter = ("created_time", "owner", "title", "content")


class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("created_time", "user", "post", "content")
    list_filter = ("created_time", "user", "post", "content")


class UserAdmin(admin.ModelAdmin):
    search_fields = (
        "username", "first_name", "last_name", "email",
    )
    list_filter = (
        "username", "first_name", "last_name", "email",
    )
